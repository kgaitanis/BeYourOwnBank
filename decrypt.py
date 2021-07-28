#!/usr/bin/env python
import binascii

from pyssss.PySSSS import decode
from io import StringIO, BytesIO
from cryptography.fernet import Fernet

from internal.password_to_key import password_to_key


if __name__ == "__main__":
    nKeys = input("Number of Keys required to decrypt: ")
    keys = []

    for i in range(nKeys):
        keys.append(raw_input("Enter Key #%s: "%i))

    keyBytes = []
    for i in range(nKeys):
        str = binascii.unhexlify(keys[i].decode('UTF-8'))
        sio = StringIO(str.decode('unicode-escape'))
        keyBytes.append(sio)

    output = BytesIO()
    decode(keyBytes, output)
    decoded = output.getvalue().decode('UTF-8')

    password = raw_input('Password:')
    fernet = Fernet(password_to_key(password))
    decrypted_secret = fernet.decrypt(output.getvalue()).decode()

    print("Here is the decrypted secret:")
    print(decrypted_secret)
