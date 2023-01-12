# Copyright © 2023 Vitaliy Zaitsev. All rights reserved.
# Licensed under the Apache License, Version 2.0
# Contacts: <dev.zaitsev@gmail.com>

import subprocess


def notify(msg: str) -> None:
    """
    The notify function is a helper function that uses the notify-send
    command to send notifications. It takes one argument, msg, which is
    the message to be sent.

    Args:
        msg: Pass the message to be displayed
    """
    command = ("notify-send", msg)
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
