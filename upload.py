import requests
import json
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = 'https://api.cacophony.org.nz/api/v1/recordings/device/TEST/group/Audio Lure Test'

filename = "test.mp4"

token = "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTAyLCJfdHlwZSI6InVzZXIiLCJpYXQiOjE2MDU0NzE1NTF9.fN1GTV2GIWn6ARkSPQnqPe8xCmgukfJjgh5em93lElM"
props = {"type": "audio"}
json_props = json.dumps(props)

with open(filename, "rb") as content:
    multipart_data = MultipartEncoder(
        fields = {"data": json_props, "file": (os.path.basename(filename), content)}
    )
    headers = {"Content-type": multipart_data.content_type, "Authorization": token}
    response = requests.request("POST", url, headers=headers, data=multipart_data)

print(response.text)