To check a directory on a remote computer for found hashes using Python, you can use the Cyware SOAR SDK for Python. Here are the steps to check a directory on a remote computer for found hashes using Cyware SOAR in Python:

1. Install the Cyware SOAR SDK for Python using pip command. Open the command prompt or terminal and run the following command:

   ```
   pip install cyapi
   ```

2. Import the `cyapi` module:

   ```
   import cyapi
   ```

3. Instantiate the `CyAPI` client by passing your Cyware SOAR API key:

   ```
   client = cyapi.CyAPI(api_key='YOUR_API_KEY')
   ```

4. Use the `run_action()` method of the `CyAPI` client to run the `CheckHash` action on the remote computer. Here is an example of how to run the `CheckHash` action:

   ```
   action_name = 'CheckHash'
   asset_name = 'remote_computer'
   asset_type = 'Windows'
   parameters = {'Directory': 'C:\\path\\to\\directory', 'Hash': 'YOUR_HASH_VALUE'}
   action_result = client.run_action(action_name, asset_name, asset_type, parameters)
   ```

   Replace 'remote_computer' with the name of the remote computer asset in Cyware SOAR. Replace 'Windows' with the type of the asset. Replace 'C:\\path\\to\\directory' with the actual path of the directory you want to search. Replace 'YOUR_HASH_VALUE' with the actual hash value you want to search for.

5. Check the result of the action in the `Action Results` object returned by the `run_action()` method:

   ```
   data = action_result.json()['ResultData']
   if 'Output' in data: