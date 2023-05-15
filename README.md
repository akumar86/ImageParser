# How to set up project locally

## Python Installation
Install the python [See instructions here](https://www.python.org/)

## Install Tesseract in your local machine

Install and setup Tesseract in your machine [See instructions here](https://tesseract-ocr.github.io/tessdoc/Installation.html)

## Set up virtual environment
`python -m venv .venv`
`source .venv/bin/activate`

## Install dependencies
`pip install -r requirements.txt`

## How to configure and run

Create a `uploaded_images` directory inside the project if not exists, this folder will contain the uploaded images

### Run the Project
`uvicorn main:app --reload` 


# How to test?
1. Go to Postman
2. Open a new tab
3. Select request type `POST`
4. Provide API url `http://localhost:8000/extract-text`
5. Select `Body` as a payload
6. Select `form-data`
7. Key should be `image`. In key section, there would be a dropdown
8. Select `File` from dropdown
9. Select a file, which you want to extract the text
10. Hit Send!


:trollface: