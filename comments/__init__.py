from pydantic import BaseModel


# Validator to publish comment
class CommentModel(BaseModel):
    comment_text: str
    user_id: int
    post_id: int


# Validator to change comment
class EditCommentModel(BaseModel):
    new_text: str
    comment_id: int