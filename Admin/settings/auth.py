from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from ..settings.config import secret
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from datetime import datetime, timedelta, timezone

oauthToken= OAuth2PasswordBearer(tokenUrl='admin/login')

#jwt token code here
def genToken(data):
    data['exp']= datetime.now(timezone.utc)+ timedelta(minutes=secret.expire)
    token= jwt.encode(data, secret.secret_key, algorithm="HS256")
    return token

def authenticate(token: str = Depends(oauthToken)):
    try:
        data= jwt.decode(token, secret.secret_key, algorithms=['HS256'])
        return data
    except JWTError as err:
        print(err)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid or expired")

#user password encrypt verify
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encrypt_pwd(pwd):
    return pwd_context.hash(pwd)

def verify_pwd(pwd, hashed_pwd):
    return pwd_context.verify(pwd, hashed_pwd)
