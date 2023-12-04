from fastapi import APIRouter
from comments import CommentModel, EditCommentModel
from database.commentsservice import add_comment_db, edit_comment_db, delete_comment_db, get_post_comments

comment_router = APIRouter(prefix='/comment', tags=['Work on comments'])


# Request on comment publications
@comment_router.post('/add_comment')
async def add_comment(data: CommentModel):
    pass


# Request to change comments
@comment_router.put('/edit_comment')
async def edit_comment(data: EditCommentModel):
    pass


# Request to delete comment
async def delete_comment(comment_id: int):
    pass


# Request to get comments to specific post
@comment_router.get('/get_comments')
async def get_comments(post_id: int):
    passmd