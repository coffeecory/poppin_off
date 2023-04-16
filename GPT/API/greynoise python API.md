Here's an example on how to call the GrayNoise API in Python 3:

```python
import requests
import json

GRAYNOISE_API_URL = "https://api.greynoise.io/v2/noise/context/%s"

ip_address = "8.8.8.8" # replace with the IP address you want to check

try:
    url = GRAYNOISE_API_URL % ip_address
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data['metadata']['status'] == "unknown":
            print("No information available for %s" % ip_address)
        elif data['metadata']['status'] == "not_found":
            print("%s is not found in GrayNoise's database" % ip_address)
        else:
            print("%s is found in GrayNoise's database. Classification: %s" % (ip_address, data['metadata']['classification']))
    else:
        print("Failed to get information from GrayNoise API. Status code: %d" % response.status_code)
except Exception as e:
    print("An error occurred while calling GrayNoise API: %s" % str(e))
```

This code uses the `requests` library to make a web request to the GrayNoise API and returns the classification of the IP address using the `/noise/context/{ip}` endpoint. 

You will need to replace `8.8.8.8` with the IP address you want to check, and your API key and secret with your own GrayNoise API credentials.
