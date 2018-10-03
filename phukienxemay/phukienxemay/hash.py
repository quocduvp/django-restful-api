from django.contrib.auth.hashers import make_password, check_password
import jwt
from phukienxemay.settings import SECRET_EMAIL_KEY


def hash_password(text):
    hashed = make_password(text)
    return hashed


def check_hash_password(text, hash):
    return check_password(text, hash)


def encode_text(text):
    encode = jwt.encode({'text':text}, SECRET_EMAIL_KEY, algorithm='HS256')
    return encode.decode('utf-8')


def decode_text(token):
    try:
        decode = jwt.decode(token, SECRET_EMAIL_KEY)
        return decode
    except jwt.ExpiredSignatureError:
        # Signature has expired
        raise Exception("Signature has expired")
