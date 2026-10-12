from slowapi import Limiter
from fastapi import Request
from slowapi.util import get_remote_address

def get_user_id_key(request: Request):
    user = request.state.user
    return str(user.id)

limiter = Limiter(key_func=get_remote_address)