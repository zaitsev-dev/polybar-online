# Copyright © 2023 Vitaliy Zaitsev. All rights reserved.
# Licensed under the Apache License, Version 2.0
# Contacts: <dev.zaitsev@gmail.com>

from . import settings
from .loop import connection_loop
from .status_printer import StatusPrinter
from .utils import parse_args


def main():
    """The main function is the entry point of a program"""
    args = parse_args(settings.ARGPARSE_DESCRIPTION, settings.ARGPARSE_ARGUMENTS)
    printer = StatusPrinter(
        online_str=args.online_icon,
        offline_str=args.offline_icon,
        online_notification=settings.ONLINE_MESSAGE,
        offline_notification=settings.OFFLINE_MESSAGE,
    )
    connection_loop(
        printer,
        is_notify=args.notify,
        check_interval=args.check_interval,
        retry_interval=args.retry_interval,
    )


if __name__ == "__main__":
    main()
