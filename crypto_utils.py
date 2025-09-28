#Erbet Gomez Bohorquez 69338 Tercer Semestre ITS
import bcrypt

def hash_password(plain_password: str) -> bytes:
    """Devuelve el hash bcrypt (bytes)."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_password.encode('utf-8'), salt)

def verify_password(plain_password: str, hashed: bytes) -> bool:
    """Verifica una contraseña contra un hash bcrypt."""
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed)
    except ValueError:
        return False
