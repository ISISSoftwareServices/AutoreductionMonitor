# ############################################################################### #
# Autoreduction Repository : https://github.com/ISISScientificComputing/autoreduce
#
# Copyright &copy; 2020 ISIS Rutherford Appleton Laboratory UKRI
# SPDX - License - Identifier: GPL-3.0-or-later
# ############################################################################### #
"""
A module for gathering and persistently storing data collected about Autoreductions state and
performance.
"""

# Internal Dependencies

# External Dependencies
import sys
import os
import logging
import inspect


class GetLogger:
    """Class to initialise logging when called"""
    def __init__(self, log_level=None, log_file_name=None, print_to_console=None):
        """
        :param log_level: (str) level to log
        :param log_file_name: (str) filename to log too - Default is script name calling GetLogger
        :param print_to_console: (Bool) True or False to stream log to console when running
        """
        # self.log_level = log_level
        # self.message = message

        # Set log sile name equal to callers filename with .log extension appended
        if not log_file_name:
            caller_frame = inspect.stack()[1]
            caller_filename = caller_frame.filename
            self.log_file_name = f"{os.path.splitext(os.path.basename(caller_filename))[0]}.log"
        else:
            self.log_file_name = log_file_name

        # Don't print logs to output if None
        if not print_to_console:
            self.print_to_console = False
        else:
            self.print_to_console = print_to_console

        if not log_level:
            self.log_level = 'DEBUG'
        else:
            self.log_level = log_level.upper()

        self.logger = self.create_logger()

    @staticmethod
    def set_log_level(log_level):
        """Sets log level"""

        return getattr(sys.modules[logging.__name__], log_level)

    @staticmethod
    def set_log_format():
        """Set log format"""
        return logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

    def set_stream_handler(self):
        """adds stream handler to output to terminal"""
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.set_log_format())
        return stream_handler

    def create_logger(self):
        """Create logger"""
        logger = logging.getLogger(__name__)
        logger.setLevel(self.set_log_level(self.log_level))

        file_handler = logging.FileHandler(self.log_file_name)
        file_handler.setFormatter(self.set_log_format())
        # file_handler.setFormatter()

        if self.print_to_console:
            logger.addHandler(self.set_stream_handler())

        logger.addHandler(file_handler)

        return logger
