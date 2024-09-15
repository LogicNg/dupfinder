import logging
import os
import shutil

from const import PHOTO_DIR, PROCESSED_DIR

logging.disable(logging.CRITICAL)


if os.path.exists(PHOTO_DIR):
    print("Initializing...")

    from utils.copy_filtered import copy_filtered
    from utils.pick_photos import pick_photos
    from utils.preprocess import preprocess

    print("Getting the images ready")
    preprocess()

    print("Finding similar photos and picking the best ones")
    photos = pick_photos()

    print('Copying the photos to the "filtered" folder')
    copy_filtered(photos)

    print("Cleaning up")
    shutil.rmtree(PROCESSED_DIR)

    print('Done! Check the "filtered" folder and see the result')
else:
    print("Please create a folder called 'photos' and put your photos in it")
    input("Press any key to continue...")
