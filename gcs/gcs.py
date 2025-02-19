from google.cloud import storage


class Bucket:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def write(self, blob_name, content):
        """Write and read a blob from GCS using file-like IO"""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"

        # The ID of your new GCS object
        # blob_name = "storage-object-name"

        storage_client = storage.Client()
        bucket = storage_client.bucket(self.bucket_name)
        blob = bucket.blob(blob_name)

        # Mode can be specified as wb/rb for bytes mode.
        # See: https://docs.python.org/3/library/io.html
        with blob.open("w") as f:
            f.write(content)
            return

    def read(self, blob_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(self.bucket_name)
        blob = bucket.blob(blob_name)
        with blob.open("r") as f:
            return f.read()
