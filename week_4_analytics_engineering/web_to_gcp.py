import io
import os
#import requests
import urllib.request 
from pathlib import Path

import pandas as pd
import pyarrow
from google.cloud import storage

"""
Pre-reqs: 
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

# services = ['fhv','green','yellow']
init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download'
# switch out the bucketname
BUCKET = os.environ.get("GCP_GCS_BUCKET", "dtc-data-lake-bucketname")


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    # storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    # storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


def web_to_gcs(year, service):
    for i in range(12):

        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # construct the path, filename and url
        local_path = Path(f"data/{service}/")
        local_path.mkdir(parents=True, exist_ok=True)

        file_name = f"{service}_tripdata_{year}-{month}"
        local_path = local_path / f"{file_name}.csv.gz"
        final_url = f"{init_url}/{service}/{file_name}.csv.gz"
        print(f"Downloading from: {final_url}")
    
        # download file directly
        local_filename, _ = urllib.request.urlretrieve(final_url, local_path)
        print(f"Saved to: ./{local_filename}")

        # upload it to gcs 
        upload_to_gcs(BUCKET, f"data/{service}/{file_name}.csv.gz", local_path)
        print(f"GCS: data/{service}/{file_name}.csv.gz")


# web_to_gcs('2019', 'green')
# web_to_gcs('2020', 'green')
# web_to_gcs('2019', 'yellow')
# web_to_gcs('2020', 'yellow')

web_to_gcs('2019', 'fhv')
web_to_gcs('2020', 'fhv')