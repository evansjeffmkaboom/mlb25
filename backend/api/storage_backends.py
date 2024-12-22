from storages.backends.s3boto3 import S3Boto3Storage

class IDriveE2Storage(S3Boto3Storage):
    bucket_name = 'mlb-player-images'
    custom_domain = f'https://app.idrivee2.com/region/CA/buckets/mlb-player-images'
