# Copyright © 2023 Vitaliy Zaitsev. All rights reserved.
# Licensed under the Apache License, Version 2.0
# Contacts: <dev.zaitsev@gmail.com>


def flush_print(*args, **kwargs):
    """
    The flush_print function prints to the console and forces all output to be written immediately.
    This is helpful when running a script in the background, such as with .gitignore -i.

    Args:
        *args: Pass a non-keyword, variable-length argument list
        **kwargs: Pass keyword, variable-length arguments to the function

    Returns:
        None
    """
    print(*args, **kwargs, flush=True)
