# import the necessary packages
import os
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# start the timer to measure the time it takes to process all of the images

path_pdf = "input/pdf"
img_path = "input/images"
output_path = "output"


def grayscale_image(image) -> Image:
    # convert the pillow image to grayscale
    return image.convert("L")


def process_pdfs() -> None:
    # check if in the data folder there are any pdfs
    # if there are, convert them to images
    pdfs = Path(path_pdf).rglob("*.pdf")

    # check if the generator is empty

    for f in pdfs:
        if f is None:
            break

        # new subfolder for each pdf
        Path(os.path.join(img_path, f.stem)).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(output_path, f.stem)).mkdir(parents=True, exist_ok=True)

        images = convert_from_path(f"{f}")
        for i, image in enumerate(images):
            image.save(f"{img_path}/{f.stem}/{f.stem}_{i}.jpg", "JPEG")

        # copy all images in the data folder to the images folder
        images = Path(path_pdf).rglob("*.jpg")
        for f in images:
            shutil.copy(f, "images")
        images = Path(path_pdf).rglob("*.png")
        for f in images:
            shutil.copy(f, "images")
        images = Path(path_pdf).rglob("*.jpeg")
        for f in images:
            shutil.copy(f, "images")


def ocr() -> None:
    # collect all files in the images folder
    images = Path(img_path).rglob("*.*")

    # iterate over all of the images
    for f in images:
        # load the image as a PIL/Pillow image, apply OCR, and then store the text in a file
        print(f"Processing {f}")
        text = pytesseract.image_to_string(Image.open(f).convert("L"), lang="deu")

        # write the text to a file
        with open(f"{output_path}/{f.parents[0].name}/{f.stem}.txt", "w") as file:
            file.write(text)
