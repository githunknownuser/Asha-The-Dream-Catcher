import logging
import os
from datetime import datetime


class Logger:
    def __init__(self, log_file='asha_logs.log'):
        self.log_file = log_file
        self.logger = logging.getLogger('AshaLogger')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(self.log_file)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def log_debug(self, message):
        """Logs debug-level messages."""
        self.logger.debug(message)

    def log_info(self, message):
        """Logs info-level messages."""
        self.logger.info(message)

    def log_warning(self, message):
        """Logs warning-level messages."""
        self.logger.warning(message)

    def log_error(self, message):
        """Logs error-level messages."""
        self.logger.error(message)

    def log_critical(self, message):
        """Logs critical-level messages."""
        self.logger.critical(message)

    def get_log_content(self):
        """Returns the content of the log file."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                return file.read()
        return ""

    def archive_log(self):
        """Archives the current log file with a timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_file = f"{self.log_file}_{timestamp}.log"
        if os.path.exists(self.log_file):
            os.rename(self.log_file, archive_file)
            self.__init__(self.log_file)
            return archive_file
        return ""

    def clear_log(self):
        """Clears the log file content."""
        if os.path.exists(self.log_file):
            open(self.log_file, 'w').close()
