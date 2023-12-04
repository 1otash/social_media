from pydantic import BaseModel


# Validator for login to account
class LoginUserValidator(BaseModel):
    email: str
    password: str


# Validator for registration
class RegisterUserValidator(BaseModel):
    name: str
    email: str
    surname: str
    phone_number: str
    city: str
    password: str


# Validator for edit user data
class EditUserValidator(BaseModel):
    user_id: int
    edit_data: str
    new_data: str