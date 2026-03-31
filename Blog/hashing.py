from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


class Hash():
    def encrypt(password:str):
        return password_hash.hash(password)
    

    def verify(hashed_password,plain_password):
     return password_hash.verify(plain_password,hashed_password)