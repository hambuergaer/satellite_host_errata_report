#!/usr/bin/env python
from passlib.hash import sha256_crypt
from cryptography.fernet import Fernet

password = "SuperSecretPassword"
key = Fernet.generate_key()
f = Fernet(key)
encrypted = f.encrypt(password)
decrypted = f.decrypt(encrypted)

print "Key: %s" % key
print "Encrypted password: %s" % encrypted
print "Decrypted password: %s" % decrypted