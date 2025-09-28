#Erbet Gomez Bohorquez 69338 Tercer Semestre ITS
from memory_db import MemoryUserDB
from json_db import JSONUserDB
import os

if __name__ == "__main__":
 print('--- Ejemplo sin archivo json (En memoria) ---')
memdb = MemoryUserDB()
    # Paso 1
memdb.add_user_plain('Erbet', '12345678')
print('Paso1: añadido Erbet con contraseña en claro')

    # Paso 2
ok_plain = memdb.check_login_plain('Erbet', '12345678')
print('Paso2: login comprobado con texto en claro ->', ok_plain)

    # Paso 3
memdb.hash_user_password('Erbet')
print('Paso3: contraseña de Erbet hasheada y reemplazada')

    # Paso 4
ok_hashed = memdb.check_login_hashed('Erbet', '12345678')
print('Paso4: login comprobado contra hash ->', ok_hashed)

print('\n--- Ejemplo con JSON (users.json) ---')
jsondb = JSONUserDB('users_demo.json')
    # borrar si existía para el ejemplo
if os.path.exists('users_demo.json'):
        os.remove('users_demo.json')
jsondb = JSONUserDB('users_demo.json')

    # Paso 1
jsondb.add_user_plain('bob', 'mypassword')
print('Paso1: añadido bob con contraseña en claro (archivo users_demo.json)')

    # Paso 2
ok_plain_json = jsondb.check_login_plain('bob', 'mypassword')
print('Paso2: login comprobado (texto en claro) ->', ok_plain_json)

    # Paso 3
jsondb.hash_user_password('bob')
print('Paso3: contraseña de bob hasheada y guardada en users_demo.json')

    # Paso 4
ok_hashed_json = jsondb.check_login_hashed('bob', 'mypassword')
print('Paso4: login comprobado contra hash (JSON) ->', ok_hashed_json)

print('\nPrueba fallida (contraseña incorrecta):', jsondb.check_login_hashed('bob', 'wrongpass'))

print('\nFichero generado: users_demo.json')
