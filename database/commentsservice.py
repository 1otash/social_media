from .models import Comment
from database import get_db
from datetime import datetime


def add_comment_db(user_id, comment_text, post_id):
    db = next(get_db())

    new_comment = Comment(user_id=user_id, comment_text=comment_text, post_id=post_id)

    db.add(new_comment)
    db.commit()

    return 'Successfully added'


def edit_comment_db(comment_id, new_comment):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    if exact_comment:
        exact_comment.comment_text = new_comment
        db.commit()

        return "Successfully edited"

    else:
        return False


def delete_comment_db(comment_id):
    db = next(get_db())

    delete_comment = db.query(Comment).filter_by(id=comment_id).first()

    if delete_comment:
        db.delete(delete_comment)
        db.commit()

        return 'Successfully deleted'

    else:
        return False


# Get all comment of exact post
def get_post_comments(post_id):
    db = next(get_db())

    post_comment = db.query(Comment).filter_by(post_id=post_id).first()

    return post_comment