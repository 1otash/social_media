from pydantic import BaseModel


# Validator post publisher
class PublicPostValidator(BaseModel):
    user_id: int
    post_text: str


# Validator to change text for post
class EditPOstValidator(BaseModel):
    post_id: int
    new_text: str
    user_id: int