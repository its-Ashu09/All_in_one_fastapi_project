
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer # Automatically header se token extract karega

from Blog import token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str = Depends(oauth2_scheme)):
     credentials_exception = HTTPException(  
        status_code=status.HTTP_401_UNAUTHORIZED, #if token is invalid then it will return 401 error
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    
    #now token automaticaly goes into data variable and we have to verify it.
     return token.verify_token(data,credentials_exception)
    