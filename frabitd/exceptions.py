# (c) 2020 frabit-server Project maintained and limited by FrabiTech < blylei.info@gmail.com >
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This file is part of frabit-server
#

class BarmanException(Exception):
    """
    The base class of all other barman exceptions
    """


class ConfigurationException(BarmanException):
    """
    Base exception for all the Configuration errors
    """


class CommandException(BarmanException):
    """
    Base exception for all the errors related to
    the execution of a Command.
    """


class CompressionException(BarmanException):
    """
    Base exception for all the errors related to
    the execution of a compression action.
    """


class PostgresException(BarmanException):
    """
    Base exception for all the errors related to PostgreSQL.
    """


class BackupException(BarmanException):
    """
    Base exception for all the errors related to the execution of a backup.
    """


class WALFileException(BarmanException):
    """
    Base exception for all the errors related to WAL files.
    """
    def __str__(self):
        """
        Human readable string representation
        """
        return "%s:%s" % (self.__class__.__name__,
                          self.args[0] if self.args else None)


class HookScriptException(BarmanException):
    """
    Base exception for all the errors related to Hook Script execution.
    """


class LockFileException(BarmanException):
    """
    Base exception for lock related errors
    """


class SyncException(BarmanException):
    """
    Base Exception for synchronisation functions
    """


class DuplicateWalFile(WALFileException):
    """
    A duplicate WAL file has been found
    """


class MatchingDuplicateWalFile(DuplicateWalFile):
    """
    A duplicate WAL file has been found, but it's identical to the one we
    already have.
    """


class SshCommandException(CommandException):
    """
    Error parsing ssh_command parameter
    """


class UnknownBackupIdException(BackupException):
    """
    The searched backup_id doesn't exists
    """


class BackupInfoBadInitialisation(BackupException):
    """
    Exception for a bad initialization error
    """


class SyncError(SyncException):
    """
    Synchronisation error
    """


class SyncNothingToDo(SyncException):
    """
    Nothing to do during sync operations
    """


class SyncToBeDeleted(SyncException):
    """
    An incomplete backup is to be deleted
    """


class CommandFailedException(CommandException):
    """
    Exception representing a failed command
    """


class CommandMaxRetryExceeded(CommandFailedException):
    """
    A command with retry_times > 0 has exceeded the number of available retry
    """


class RsyncListFilesFailure(CommandException):
    """
    Failure parsing the output of a "rsync --list-only" command
    """


class DataTransferFailure(CommandException):
    """
    Used to pass failure details from a data transfer Command
    """

    @classmethod
    def from_command_error(cls, cmd, e, msg):
        """
        This method build a DataTransferFailure exception and report the
        provided message to the user (both console and log file) along with
        the output of the failed command.

        :param str cmd: The command that failed the transfer
        :param CommandFailedException e: The exception we are handling
        :param str msg: a descriptive message on what we are trying to do
        :return DataTransferFailure: will contain the message provided in msg
        """
        try:
            details = msg
            details += "\n%s error:\n" % cmd
            details += e.args[0]['out']
            details += e.args[0]['err']
            return cls(details)
        except (TypeError, NameError):
            # If it is not a dictionary just convert it to a string
            from barman.utils import force_str
            return cls(force_str(e.args))


class CompressionIncompatibility(CompressionException):
    """
    Exception for compression incompatibility
    """


class FsOperationFailed(CommandException):
    """
    Exception which represents a failed execution of a command on FS
    """


class LockFileBusy(LockFileException):
    """
    Raised when a lock file is not free
    """


class LockFilePermissionDenied(LockFileException):
    """
    Raised when a lock file is not accessible
    """


class LockFileParsingError(LockFileException):
    """
    Raised when the content of the lockfile is unexpected
    """


class ConninfoException(ConfigurationException):
    """
    Error for missing or failed parsing of the conninfo parameter (DSN)
    """


class PostgresConnectionError(PostgresException):
    """
    Error connecting to the PostgreSQL server
    """
    def __str__(self):
        # Returns the first line
        if self.args and self.args[0]:
            from barman.utils import force_str
            return force_str(self.args[0]).splitlines()[0].strip()
        else:
            return ''


class PostgresAppNameError(PostgresConnectionError):
    """
    Error setting application name with PostgreSQL server
    """


class PostgresSuperuserRequired(PostgresException):
    """
    Superuser access is required
    """


class BackupFunctionsAccessRequired(PostgresException):
    """
    Superuser or access to backup functions is required
    """


class PostgresIsInRecovery(PostgresException):
    """
    PostgreSQL is in recovery, so no write operations are allowed
    """


class PostgresUnsupportedFeature(PostgresException):
    """
    Unsupported feature
    """


class PostgresDuplicateReplicationSlot(PostgresException):
    """
    The creation of a physical replication slot failed because
    the slot already exists
    """


class PostgresReplicationSlotsFull(PostgresException):
    """
    The creation of a physical replication slot failed because
    the all the replication slots have been taken
    """


class PostgresReplicationSlotInUse(PostgresException):
    """
    The drop of a physical replication slot failed because
    the replication slots is in use
    """


class PostgresInvalidReplicationSlot(PostgresException):
    """
    Exception representing a failure during the deletion of a non
    existent replication slot
    """


class TimeoutError(CommandException):
    """
    A timeout occurred.
    """


class ArchiverFailure(WALFileException):
    """
    Exception representing a failure during the execution
    of the archive process
    """


class BadXlogSegmentName(WALFileException):
    """
    Exception for a bad xlog name
    """


class BadHistoryFileContents(WALFileException):
    """
    Exception for a corrupted history file
    """


class AbortedRetryHookScript(HookScriptException):
    """
    Exception for handling abort of retry hook scripts
    """
    def __init__(self, hook):
        """
        Initialise the exception with hook script info
        """
        self.hook = hook

    def __str__(self):
        """
        String representation
        """
        return ("Abort '%s_%s' retry hook script (%s, exit code: %d)" % (
                self.hook.phase, self.hook.name,
                self.hook.script, self.hook.exit_status))


class RecoveryException(BarmanException):
    """
    Exception for a recovery error
    """


class RecoveryTargetActionException(RecoveryException):
    """
    Exception for a wrong recovery target action
    """


class RecoveryStandbyModeException(RecoveryException):
    """
    Exception for a wrong recovery standby mode
    """


class RecoveryInvalidTargetException(RecoveryException):
    """
    Exception for a wrong recovery target
    """
