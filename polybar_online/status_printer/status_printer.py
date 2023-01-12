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
        The function is called when an instance of the class is created.

        Args:
            self: Refer to the object itself
            online_str: The output string that will be displayed when
                the device is online
            offline_str: The output string that will be displayed when
                the device is online
            online_notification: The text that will be sent to the user
                when they are online
            offline_notification: The text that will be sent to the user
                when they are offline
        """
        self._online_output: str = online_str
        self._offline_output: str = offline_str
        self._online_notification = online_notification
        self._offline_notification = offline_notification

    def _print_status(self, status: bool, is_notify: bool) -> None:
        flush_print(self._online_output if status else self._offline_output)
        if is_notify:
            notify(self._online_notification if status else self._offline_notification)

    def print_online_status(self, is_notify: bool) -> None:
        self._print_status(status=True, is_notify=is_notify)

    def print_offline_status(self, is_notify: bool) -> None:
        self._print_status(status=False, is_notify=is_notify)
