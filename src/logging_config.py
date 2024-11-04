import logging
import settings


def setup_logging(log_file=settings.load_value_from_json_file("logfilename")):
    # Create a logger
    logger = logging.getLogger()
    # get loglevel from environment
    loglevel = settings.load_value_from_json_file("loglevel")
    if loglevel == "DEBUG":
        logger.setLevel(logging.DEBUG)
    if loglevel == "INFO":
        logger.setLevel(logging.INFO)
    if loglevel == "ERROR":
        logger.setLevel(logging.ERROR)

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    if loglevel == "DEBUG":
        file_handler.setLevel(logging.DEBUG)
    if loglevel == "INFO":
        file_handler.setLevel(logging.INFO)
    if loglevel == "ERROR":
        file_handler.setLevel(logging.ERROR)

    # Create a formatter and set it for the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)


# Call the setup_logging function to configure logging
settings.create_config()  # be sure, logfile is set
setup_logging()
