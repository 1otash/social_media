from fastapi import APIRouter
from user import LoginUserValidator, RegisterUserValidator, EditUserValidator
from database.userservice import login_user_db, register_user_db, get_exact_user_db, get_all_users_db


user_router = APIRouter(prefix='/user', tags=['Control users'])

# Login

@user_router.post('/login')
async def login_user(data: LoginUserValidator):
    result = login_user_db(**data.model_dump())
    return {'message': result}


# Registration
@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    result = register_user_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'User with such email is already here'}


# Request to get user info
@user_router.get('/get_user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()

        return {'message': result}
    else:
        result = get_exact_user_db(user_id)
        return {'message': result}