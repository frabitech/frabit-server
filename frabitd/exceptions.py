# (c) 2020 frabit-server Project maintained and limited by FrabiTech < blylei.info@gmail.com >
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This file is part of frabit-server
#

class FrabitdException(Exception):
    """
    The base class of all other barman exceptions
    """


class ConfigurationException(FrabitdException):
    """
    Base exception for all the Configuration errors
    """


class CommandException(FrabitdException):
    """
    Base exception for all the errors related to
    the execution of a Command.
    """


class CompressionException(FrabitdException):
    """
    Base exception for all the errors related to
    the execution of a compression action.
    """


class ProcessException(FrabitdException):
    """
    Base exception for all the errors related to PostgreSQL.
    """


class BackupException(FrabitdException):
    """
    Base exception for all the errors related to the execution of a backup.
    """


class WALFileException(FrabitdException):
    """
    Base exception for all the errors related to WAL files.
    """
    def __str__(self):
        """
        Human readable string representation
        """
        return "%s:%s" % (self.__class__.__name__,
                          self.args[0] if self.args else None)


class HookScriptException(FrabitdException):
    """
    Base exception for all the errors related to Hook Script execution.
    """


class LockFileException(FrabitdException):
    """
    Base exception for lock related errors
    """


class SyncException(FrabitdException):
    """
    Base Exception for synchronisation functions
    """

