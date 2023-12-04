from fastapi import APIRouter, UploadFile, Body
from post import PublicPostValidator, EditPOstValidator
from database.postservice import add_post_db, add_post_photo_db, edit_post_db, delete_post_db, get_exact_post_db

post_router = APIRouter(prefix='/user_post', tags=['Work with publications'])


# Request on post publication
@post_router.post('/public_post')
async def public_post(data: PublicPostValidator):
    result = add_post_db(**data.model_dump())
    return {'message': result}


# Request to change text of publication
@post_router.put('/change_post')
async def change_post(data: EditPOstValidator):
    result = edit_post_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}


@post_router.delete('/delete_post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}


# Request to get all publications
@post_router.get('/get_all_posts')
async def get_all_posts(post_id: int):
    result = get_all_posts(post_id)
    return {'message': result}


# Request to add photo to post
@post_router.post('/add_photo')
async def add_photo(post_id: int = Body(),
                    user_id: int = Body(),
                    photo_file: UploadFile = None
                    ):
    photo_path = f'/media/{photo_file.filename}'
    try:
        # Save photos in media directory
        with open(f'media/{photo_file.filename}', 'wb') as file:
            user_photo = await photo_file.read()
            file.write(user_photo)
            # Save references of photo to db
            result = add_post_photo_db(post_id=post_id,
                                       photo_file=photo_path)
    except Exception as error:
        result=error
    return {'message': result}


# Get exact post
@post_router.get('/get_exact_post')
async def get_post(post_id: int):
    result = get_exact_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return 'Post not found'


