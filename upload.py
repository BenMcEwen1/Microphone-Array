import requests
import json
import os
from requests_toolbelt import MultipartEncoder
import parameters
from datetime import datetime

current_date = datetime.now()
print(current_date.isoformat())

def upload_recording(filename, DOA):
    # Upload the recordings to the Cacophony server
   
    props = {"type": "audio", "duration": 60, "additionalMetaData": DOA, "recordingDateTime": current_date.isoformat()}

    json_props = json.dumps(props)

    with open(filename, "rb") as content:
        multipart_data = MultipartEncoder(
            fields = {"data": json_props, "file": (os.path.basename(filename), content)}
        )
        headers = {"Content-type": multipart_data.content_type, "Authorization": parameters.user_token}
        response = requests.request("POST", parameters.upload, headers=headers, data=multipart_data)

    print(response.text)


