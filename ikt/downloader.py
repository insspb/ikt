from pathlib import Path

import requests

from ikt import logger
from ikt.constants import pre_trained_models

storage = Path("pre_trained_models")


def download_file(filename, url, storage_dir):
    """Downloads file to storage directory."""
    logger.debug("Downloading [%s].", filename)
    response = requests.get(url)

    if response.status_code == 200:
        with open(Path(storage_dir, filename), 'wb') as fd:
            for chunk in response.iter_content(chunk_size=128):
                fd.write(chunk)
        logger.debug("Download [%s] success.", filename)
        return True

    logger.debug("Download [%s] failed.", filename)
    return False


def download_models():
    """Downloads pre-trained models from ImageAI GitHub."""
    logger.info(
        "Scheduling pre-trained models download to [%s]", Path(storage).absolute()
    )
    if not Path(storage).exists():
        logger.debug("Path [%s] did not exist, creating new.", Path(storage).absolute())
        Path(storage).mkdir()

    for filename, url in pre_trained_models.items():
        if Path(storage, filename).exists():
            logger.debug(
                "File [%s] exist, skipping.", Path(storage, filename).absolute()
            )

            continue

        download_file(filename, url, storage)
