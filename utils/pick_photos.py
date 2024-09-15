import os

from imagededup.methods import CNN

from const import PROCESSED_DIR


def pick_photos():
    encoder = CNN()

    duplicates = encoder.find_duplicates_to_remove(
        image_dir=PROCESSED_DIR, min_similarity_threshold=0.85
    )

    photos = set(os.listdir(PROCESSED_DIR))
    duplicates = set(duplicates)
    selected = photos - duplicates
    return selected
