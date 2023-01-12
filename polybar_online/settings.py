# Copyright © 2023 Vitaliy Zaitsev. All rights reserved.
# Licensed under the Apache License, Version 2.0
# Contacts: <dev.zaitsev@gmail.com>

from argparse import BooleanOptionalAction

DEFAULT_ONLINE_ICON: str = "度"
DEFAULT_OFFLINE_ICON: str = "ﴹ"

ONLINE_MESSAGE: str = "Internet connection restored"
OFFLINE_MESSAGE: str = "Internet connection is lost"

ARGPARSE_DESCRIPTION: str = (
    "Module script for Polybar that checks connection to the Internet"
)
ARGPARSE_ARGUMENTS: tuple = (
    {
        "name_or_flags": ["-n", "--notify"],
        "action": BooleanOptionalAction,
        "help": "send a notification if the internet connection is broken",
        "default": False,
    },
    {
        "name_or_flags": ["--online-icon"],
        "help": f"icon that will be displayed when the Internet connection is available (default: {DEFAULT_ONLINE_ICON})",
        "default": DEFAULT_ONLINE_ICON,
        "type": str,
    },
    {
        "name_or_flags": ["--offline-icon"],
        "help": f"icon that will be displayed when there is no Internet connection (default: {DEFAULT_OFFLINE_ICON})",
        "default": DEFAULT_OFFLINE_ICON,
        "type": str,
    },
    {
        "name_or_flags": ["-ci", "--check-interval"],
        "help": "Interval between checks (in seconds)",
        "default": 15,
        "type": int,
    },
    {
        "name_or_flags": ["-ri", "--retry-interval"],
        "help": "Interval between checks when Internet connection is unavailable (in seconds)",
        "default": 1,
        "type": int,
    },
)
