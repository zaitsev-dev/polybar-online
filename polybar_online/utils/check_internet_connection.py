# Copyright © 2023 Vitaliy Zaitsev. All rights reserved.
# Licensed under the Apache License, Version 2.0
# Contacts: <dev.zaitsev@gmail.com>

from http import client
from socket import gaierror


def check_internet_connection(host: str = "google.com") -> bool:
    """
    The function checks if the device is connected to the internet. It does
    this by attempting to connect to google.com and excepting connection errors
    """
    connection = client.HTTPConnection(host=host, timeout=5)
    try:
        connection.request("HEAD", "/")
    except (client.HTTPException, gaierror):
        return False
    finally:
        connection.close()
    return True
