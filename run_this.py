from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('key.key','wb') as keyfile:
    keyfile.write(key)

with open('key.key','rb') as keyfile:
    key = keyfile.read()


f = Fernet(key)

with open('test.db','rb') as original_file:
    original = original_file.read()

encrypted_file = f.encrypt(original)

with open('test.db','wb') as encrypted:
    encrypted.write(encrypted_file)


