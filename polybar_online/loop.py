# Copyright © 2023 Vitaliy Zaitsev. All rights reserved.
# Licensed under the Apache License, Version 2.0
# Contacts: <dev.zaitsev@gmail.com>


from time import sleep

from .status_printer import StatusPrinter
from .utils import check_internet_connection


def connection_loop(
    printer: StatusPrinter,
    is_notify: bool,
    check_interval: int,
    retry_interval: int,
) -> None:
    """
    The connection_loop function is the main loop of the program. It checks if there is an internet connection,
    and if not it prints a notification and waits for an internet connection to return. If there is an internet
    connection, it prints a notification that says that you are online.

    Args:
        printer: Print the status of the internet connection
        is_notify: Determine whether to notify the user of a change in status
        check_interval: Set the time interval between each check
        retry_interval: Set the time interval between each check when the connection is down

    Returns:
        None
    """
    prev_status = None
    while True:
        status = check_internet_connection()
        if not status:
            printer.print_offline_status(is_notify=is_notify)
            while not check_internet_connection():
                sleep(retry_interval)
            status = True
            printer.print_online_status(is_notify=is_notify)
        elif not prev_status:
            printer.print_online_status(is_notify=False)
        sleep(check_interval)
        prev_status = status
