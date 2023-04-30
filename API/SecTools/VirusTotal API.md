```Python 

import requests


def get_virustotal_api_key():
    """Get the VirusTotal API key from a file.

    :return: The API key or None if not found.
    """
    try:
        with open('virustotal-api-key', 'r') as f:
            return f.readline().strip()  # Remove newlines and spaces at the end of line.

    except FileNotFoundError:  # If no virustotal-api-key file is found, return None to let user know that they need one.

        print("Couldn't find virustotal-api-key file.")

        return None
```

