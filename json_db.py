#Erbet Gomez Bohorquez 69338 Tercer Semestre ITS
import json, os, base64
from crypto_utils import hash_password, verify_password

class JSONUserDB:
    """DB simple en archivo JSON."""

    def __init__(self, filename: str = 'users.json'):
        self.filename = filename
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                self._data = json.load(f)
        else:
            self._data = {}

    def _save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self._data, f, indent=2, ensure_ascii=False)

    # Paso 1
    def add_user_plain(self, username: str, password_plain: str) -> None:
        self._data[username] = {'password': password_plain, 'hashed': False}
        self._save()

    # Paso 2
    def check_login_plain(self, username: str, password_plain: str) -> bool:
        entry = self._data.get(username)
        return entry and not entry['hashed'] and entry['password'] == password_plain

    # Paso 3
    def hash_user_password(self, username: str) -> bool:
        entry = self._data.get(username)
        if not entry or entry['hashed']:
            return False
        plain = entry['password']
        hashed_b64 = base64.b64encode(hash_password(plain)).decode('ascii')
        self._data[username] = {'password': hashed_b64, 'hashed': True}
        self._save()
        return True

    # Paso 4
    def check_login_hashed(self, username: str, password_plain: str) -> bool:
        entry = self._data.get(username)
        if not entry:
            return False
        if entry['hashed']:
            try:
                hashed_bytes = base64.b64decode(entry['password'])
                return verify_password(password_plain, hashed_bytes)
            except Exception:
                return False
        return entry['password'] == password_plain
