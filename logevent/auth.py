from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTErroe, jwt
from passlib.context import CryptContext
from fastapi import HttpException, Depends, status
from pony.orm import db_Session
from .database import Usuario

SECRET_KEY = 'secret-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypy'], deprecated= 'auto')

def create_access_token(data: dict, expires_delta=timedelta | None=None)
    pass