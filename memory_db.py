#Erbet Gomez Bohorquez 69338 Tercer Semestre ITS
from typing import Dict
from crypto_utils import hash_password, verify_password

class MemoryUserDB:
    """Base de datos en memoria con soporte de contraseñas en claro y hasheadas."""

    def __init__(self):
        self.users: Dict[str, object] = {}

    # Paso 1
    def add_user_plain(self, username: str, password_plain: str) -> None:
        self.users[username] = password_plain

    # Paso 2
    def check_login_plain(self, username: str, password_plain: str) -> bool:
        stored = self.users.get(username)
        return isinstance(stored, str) and stored == password_plain

    # Paso 3
    def hash_user_password(self, username: str) -> bool:
        stored = self.users.get(username)
        if stored is None:
            return False
        if isinstance(stored, bytes):
            return True  # ya está hasheada
        if isinstance(stored, str):
            self.users[username] = hash_password(stored)
            return True
        return False

    # Paso 4
    def check_login_hashed(self, username: str, password_plain: str) -> bool:
        stored = self.users.get(username)
        if isinstance(stored, bytes):
            return verify_password(password_plain, stored)
        if isinstance(stored, str):
            return stored == password_plain
        return False
