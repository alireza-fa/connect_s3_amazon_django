import boto3
from django.conf import settings


class Bucket:
    BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME

    def __init__(self):
        session = boto3.session.Session()
        self.conn = session.client(
            service_name=settings.AWS_SERVICE_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL
        )

    def get_objects(self):
        result = self.conn.list_objects_v2(
            Bucket=self.BUCKET_NAME
        )
        if result['KeyCount']:
            return result['Contents']

    def delete_object(self, filename):
        self.conn.delete_object(
            Bucket=self.BUCKET_NAME, Key=filename
        )
        return True


bucket = Bucket()
