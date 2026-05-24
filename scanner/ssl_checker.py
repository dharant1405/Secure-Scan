import ssl
import socket
from datetime import datetime


def check_ssl(hostname):

    try:
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443)) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as ssock:

                cert = ssock.getpeercert()

                expiry_date = cert['notAfter']

                expiry = datetime.strptime(
                    expiry_date,
                    '%b %d %H:%M:%S %Y %Z'
                )

                days_left = (expiry - datetime.now()).days

                return {
                    "valid": True,
                    "expiry_date": expiry_date,
                    "days_left": days_left
                }

    except Exception as e:

        return {
            "valid": False,
            "error": str(e)
        }