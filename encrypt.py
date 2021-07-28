#!/usr/bin/env python
import binascii
import qrcode
import os

from io import BytesIO
from pyssss.PySSSS import encode
from cryptography.fernet import Fernet

from internal.password_to_key import password_to_key
from internal.createPDF import createPDF

if __name__ == "__main__":
    nKeys = input("Number of Keys: ")
    minKeys = input("Number of keys required to recompose the secret: ")
    secret = raw_input("Secret: ")
    password = raw_input('Password: ')
    fernet = Fernet(password_to_key(password))
    encrypted_secret = fernet.encrypt(secret.encode())

    keys = []
    for i in range(nKeys):
      keys.append(BytesIO())

    encode(BytesIO(encrypted_secret), keys, minKeys)

    print("These are the %s keys:"%nKeys)
    for i in range(nKeys):
        print("-----------------------------------------")
        print('Key #%s:'%i)
        print("-----------------------------------------")
        key = binascii.hexlify(keys[i].getvalue()).encode('UTF-8')
        print(key)

        # generate qr code
        img_filename = 'qr.png'
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=0)
        qr.add_data(key)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(img_filename)

        # generate PDF
        createPDF(img_filename, key, 'key-%s.pdf'%i)

    # cleanup
    os.remove(img_filename)
