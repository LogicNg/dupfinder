import os
import platform
import shutil
from concurrent.futures import ThreadPoolExecutor

from imagededup.utils.image_utils import preprocess_image
from PIL import Image

from const import PHOTO_DIR, PROCESSED_DIR

IMAGE_SIZE = 480


def process_photo(photo):
    if not photo.endswith(
        (
            ".jpg",
            ".jpeg",
            ".png",
            ".bmp",
            ".mpo",
            ".ppm",
            ".tiff",
            ".gif",
            ".svg",
            ".pgm",
            ".pbm",
        )
    ):
        # print(photo)
        return

    # Read image
    image = Image.open(os.path.join(PHOTO_DIR, photo))

    width, height = image.size
    if width > height:
        target_size = (IMAGE_SIZE, int(height / width * IMAGE_SIZE))
    else:
        target_size = (int(width / height * IMAGE_SIZE), IMAGE_SIZE)

    # Preprocess image
    img = preprocess_image(image, target_size, grayscale=True)
    img = Image.fromarray(img)

    # Save processed image
    img.save(os.path.join(PROCESSED_DIR, photo))


def preprocess():
    if os.path.exists(PROCESSED_DIR):
        shutil.rmtree(PROCESSED_DIR)

    os.makedirs(PROCESSED_DIR)

    if platform.system() == "Windows":
        os.system(f"attrib +h {PROCESSED_DIR}")

    photos = os.listdir(PHOTO_DIR)

    # Use ThreadPoolExecutor to process images in parallel
    with ThreadPoolExecutor() as executor:
        # list(tqdm(executor.map(process_photo, photos), total=len(photos)))
        list(executor.map(process_photo, photos))
