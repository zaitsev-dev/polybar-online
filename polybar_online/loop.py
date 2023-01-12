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
    The connection_loop function is a loop that checks the internet
    connection every check_interval seconds. If there is no internet
    connection, it prints an offline status message to the console and waits
    for retry_interval seconds before checking again. If there is an internet
    connection, it prints an online status message to the console and then
    goes back to sleep for check_interval seconds.

    Args:
        printer: Printer object that print the status of the internet connection
        is_notify: Determine whether the program should notify the user about
            online status
        check_interval: Set the time interval in seconds between each check
        retry_interval: Set the time interval in seconds between each retry
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
