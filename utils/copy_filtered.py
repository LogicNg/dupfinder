import os
import shutil
from concurrent.futures import ThreadPoolExecutor

from const import FILTERED_DIR, PHOTO_DIR


def copy_file(img):
    shutil.copy(os.path.join(PHOTO_DIR, img), os.path.join(FILTERED_DIR, img))


def copy_filtered(photos):
    if os.path.exists(FILTERED_DIR):
        shutil.rmtree(FILTERED_DIR)

    os.makedirs(FILTERED_DIR)

    with ThreadPoolExecutor() as executor:
        executor.map(copy_file, photos)
