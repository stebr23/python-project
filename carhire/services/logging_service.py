"""
The Logging Service provides the application different levels of logging

This service should replace print statements in all instances with
the sufficient log level
"""
import carhire.constants as consts


class LoggingService:
    """
    Class for the Logging Service

    An instantiation of this class allows for the printing of statements
    depending on their logging level
    """

    def __init__(self, log_level):
        self.log_level = log_level

    def trace(self, module, message):
        """
        Prints a TRACE message to the console if the logging level is less than 3

        :param module: String of the name of the module calling the method
        :param message: String of the message to print
        """
        if self.log_level <= consts.LOG_LEVEL_TRACE:
            print("TRACE :  %s:    %s" % (module, message))

    def debug(self, module, message):
        """
        Prints a DEBUG message to the console if the logging level is less than 2

        :param module: String of the name of the module calling the method
        :param message: String of the message to print
        """
        if self.log_level <= consts.LOG_LEVEL_DEBUG:
            print("DEBUG :  %s:    %s" % (module, message))

    def warn(self, module, message):
        """
        Prints a WARN message to the console if the logging level is less than 1

        :param module: String of the name of the module calling the method
        :param message: String of the message to print
        """
        if self.log_level <= consts.LOG_LEVEL_WARN:
            print("WARN :  %s:    %s" % (module, message))

    def error(self, module, message):
        """
        Prints an ERROR message to the console if the logging level is less than 0

        :param module: String of the name of the module calling the method
        :param message: String of the message to print
        """
        if self.log_level <= consts.LOG_LEVEL_ERROR:
            print("ERROR :  %s:    %s" % (module, message))
