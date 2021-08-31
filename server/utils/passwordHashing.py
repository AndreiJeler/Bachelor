import hashlib

class PasswordHashing:
    @staticmethod
    def hash_password(password, username):
        return hashlib.pbkdf2_hmac("sha256", password.encode('utf-8'), username.encode('utf-8'), 100000, dklen=128)
