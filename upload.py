import requests
import json
import os
from requests_toolbelt import MultipartEncoder
import parameters

props = {"type": "audio"}
json_props = json.dumps(props)

def upload_recording(filename):

    with open(filename, "rb") as content:
        multipart_data = MultipartEncoder(
            fields = {"data": json_props, "file": (os.path.basename(filename), content)}
        )
        headers = {"Content-type": multipart_data.content_type, "Authorization": parameters.user_token}
        response = requests.request("POST", parameters.upload, headers=headers, data=multipart_data)

    print(response.text)