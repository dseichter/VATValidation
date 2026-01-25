# Copyright (c) 2024-2026 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import logging
import settings


def setup_logging():
    settings.create_config()
    log_file = settings.load_value_from_json_file("logfilename")

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
    
    # Suppress watchdog debug messages
    logging.getLogger('watchdog').setLevel(logging.WARNING)


# Call the setup_logging function to configure logging
setup_logging()
