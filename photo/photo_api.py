from fastapi import APIRouter, UploadFile

photo_router = APIRouter(prefix='/photo', tags=['Photos'])

@photo_router.post('/add_photo')
async def add_user_profile_photo(photo_file: UploadFile, user_id: int):
    print(photo_file.filename)
    print(photo_file.file)
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()
        file.write(user_photo)

    return {'status': 200, 'message': 'Successfully uploaded'}


@photo_router.put('/edit-photo')
async def edit_user_profile_photo(user_id: int, new_photo_file: UploadFile):
    print(new_photo_file.filename)
    print(new_photo_file.file)
    with open(f'media/{new_photo_file.filename}', 'wb') as file:
        user_photo = await new_photo_file.read()
        file.write(user_photo)

    return {'status': 200, 'message': 'Successfully uploaded'}



@photo_router.delete('/delete-photo')
async def delete_user_profile_photo(user_id: int):
    d