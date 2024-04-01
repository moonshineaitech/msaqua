import logging


def setup_logging(log_level, log_file=None):
    """
    Configures logging with different levels and optional output to a file.

    Args:
        log_level (str): The logging level (e.g., 'INFO', 'DEBUG').
        log_file (str, optional): The filename for logging output.
    """
    logging.basicConfig(level=log_level, filename=log_file, format='%(asctime)s - %(levelname)s - %(message)s')


def log_message(level, message):
    """
    Logs a message at the specified level.

    Args:
        level (int): The logging level (e.g., logging.INFO).
        message (str): The message to be logged.
    """
    logging.log(level, message)