Sure, here's an example Python script that allows you to scan a file with VirusTotal and retrieve the scan report:

```python
import requests

API_KEY = 'YOUR_API_KEY'

def scan_file(file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': API_KEY}
    files = {'file': (file_path, open(file_path, 'rb'))}
    response = requests.post(url, files=files, params=params)
    json_response = response.json()
    if json_response['response_code'] == 1:
        resource = json_response['resource']
        print(f'File has been uploaded with resource ID: {resource}')
        return resource
    else:
        print('There was a problem scanning the file. Please try again later.')
        return None

def get_file_report(resource):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': API_KEY, 'resource': resource}
    response = requests.get(url, params=params)
    json_response = response.json()
    if json_response['response_code'] == 1:
        positives = json_response['positives']
        total = json_response['total']
        print(f'File has been scanned {total} times.')
        print(f'File was found to be malicious by {positives} out of {total} scanners.')
        for scanner, data in json_response['scans'].items():
            print(f'{scanner}: {data["result"]}')
    else:
        print('No scan report found for this file. Please try scanning the file first.')

if __name__ == '__main__':
    file_path = '/path/to/file.txt'
    resource = scan_file(file_path)
    if resource is not None:
        get_file_report(resource)
```

Note: Replace the `API_KEY` constant with your VirusTotal API key and the `file_path` variable with the path to the file you wish to scan.

This script scans a file with VirusTotal by sending a POST request to the VirusTotal API endpoint to upload the file. The script then retrieves the scan report for the file by sending a GET request to the VirusTotal API with the resource ID obtained from the scan response.

You can modify this script to scan multiple files or integrate with other security automation tools for automated scanning and reporting.