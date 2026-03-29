from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


class Hash():
    def encrypt(password:str):
        return password_hash.hash(password)