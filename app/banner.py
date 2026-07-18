from app.logger import logger
from app.version import VERSION, BUILD

def show():

    logger.info("")

    logger.info("=" * 70)

    logger.info("              GOLD AI")

    logger.info("=" * 70)

    logger.info("Version : %s", VERSION)

    logger.info("Build   : %s", BUILD)

    logger.info("=" * 70)

    logger.info("")