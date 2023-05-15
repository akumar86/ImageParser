from fastapi import FastAPI, UploadFile, File
from fastapi.exceptions import HTTPException
from starlette import status
from PIL import Image
from bs4 import BeautifulSoup
import pytesseract
import time

app = FastAPI()


def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    cleaned_text = soup.get_text(separator=' ')
    return cleaned_text.replace('\n', ' ')


def is_image(file_path: str) -> bool:
    try:
        Image.open(file_path)
        return True
    except IOError:
        return False


def generate_unique_filename(original_filename: str) -> str:
    timestamp = int(time.time())
    filename, extension = original_filename.rsplit('.', 1)
    new_filename = f'{filename}_{timestamp}.{extension}'
    return new_filename


# help@getonecard.app

@app.post('/extract-text')
async def extract_text(image: UploadFile = File(...)):
    file_location = f'uploaded_images/{generate_unique_filename(image.filename)}'
    with open(file_location, 'wb') as file:
        file.write(image.file.read())

    if not is_image(file_location):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Uploaded file is not an image.',
        )

    extracted_text = pytesseract.image_to_string(Image.open(file_location))
    return {'filename': image.filename, 'text': remove_html_tags(extracted_text)}
