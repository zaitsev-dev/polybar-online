# Copyright © 2023 Vitaliy Zaitsev. All rights reserved.
# Licensed under the Apache License, Version 2.0
# Contacts: <dev.zaitsev@gmail.com>

import argparse
from argparse import Namespace


def parse_args(description: str, arguments: tuple[dict]) -> Namespace:
    """
    The parse_args function parses the arguments passed to the script.
    It returns a Namespace object containing all the arguments and their values.

    Args:
        description: Describe the program
        arguments: Pass a list of dictionaries to the add_argument function

    Returns:
        An object with the arguments as attributes
    """
    arguments = arguments[:]
    parser = argparse.ArgumentParser(description=description)
    for arg in arguments:
        flags = arg["name_or_flags"]
        del arg["name_or_flags"]
        parser.add_argument(*flags, **arg)
    return parser.parse_args()
