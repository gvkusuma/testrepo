import requests
import json

#URL for instance metadata
metadata_url = "http://54.146.3.236/latest/meta-data/"

# Function to fetch and format metadata as JSON
def get_metadata():
    metadata = {}
    try:
        response = requests.get(metadata_url)
        response.raise_for_status()
        metadata_keys = response.text.splitlines()
        for key in metadata_keys:
            key_url = metadata_url + key
            key_response = requests.get(key_url)
            metadata[key] = key_response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching metadata: {e}")
        return None
    return metadata

# Fetch instance metadata and convert it to JSON
instance_metadata = get_metadata()
if instance_metadata is not None:
    json_metadata = json.dumps(instance_metadata, indent=4)
    print(json_metadata)
