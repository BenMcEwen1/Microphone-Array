import requests
import json
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder
import parameters

props = {"type": "audio"}
json_props = json.dumps(props)

DOA_test = [1,2,3,4,5,6,7,8,9,10]
filename_test = "test2.mp4"
comment = "This is a test comment"
json_comment = json.dumps(comment)


def upload_recording(filename, DOA):
    # Upload the recordings to the Cacophony server
    json_DOA = json.dumps(DOA) 

    with open(filename, "rb") as content:
        multipart_data = MultipartEncoder(
            fields = {"data": json_props, "file": (os.path.basename(filename), content), "additionalMetadata": json_DOA, "comment": json_comment}
        )
        headers = {"Content-type": multipart_data.content_type, "Authorization": parameters.token}
        response = requests.request("POST", parameters.upload, headers=headers, data=multipart_data)

    print(response.text)

upload_recording(filename_test, DOA_test)