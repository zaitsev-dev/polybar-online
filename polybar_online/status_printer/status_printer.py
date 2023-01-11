# Copyright © 2023 Vitaliy Zaitsev. All rights reserved.
# Licensed under the Apache License, Version 2.0
# Contacts: <dev.zaitsev@gmail.com>

from .flush_print import flush_print
from .notify import notify


class StatusPrinter:
    def __init__(
        self,
        online_str: str,
        offline_str: str,
        online_notification: str,
        offline_notification: str,
    ) -> None:
        """
        The __init__ function is called when an instance of the class is created.

        Args:
            self: Refer to the object itself
            online_str: The output string that will be displayed when the device is online
            offline_str: The output string that will be displayed when the device is online
            online_notification: The text that will be sent to the user when they are online
            offline_notification: The text that will be sent to the user when they are offline

        Returns:
            None
        """
        self._online_output: str = online_str
        self._offline_output: str = offline_str
        self._online_notification = online_notification
        self._offline_notification = offline_notification

    def _print_status(self, status: bool, is_notify: bool) -> None:
        """
        The _print_status function prints the output to stdout and sends a notification.

        Args:
            self: Access the class attributes
            status: Determine whether the internet connection is up or not
            is_notify: Determine if a notification should be sent

        Returns:
            None
        """
        flush_print(self._online_output if status else self._offline_output)
        if is_notify:
            notify(self._online_notification if status else self._offline_notification)

    def print_online_status(self, is_notify: bool) -> None:
        """
        Prints the status of the user's connection to the console

        Args:
            self: Access the attributes and methods of the class in .gitignore
            is_notify: Determine whether to notify the user that they are offline

        Returns:
            None
        """
        self._print_status(status=True, is_notify=is_notify)

    def print_offline_status(self, is_notify: bool) -> None:
        """
        Prints the status of the user's connection to the console

        Args:
            self: Access the class attributes
            is_notify: Determine whether to notify the user that they are offline

        Returns:
            None
        """
        self._print_status(status=False, is_notify=is_notify)
