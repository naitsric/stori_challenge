import os

from chalice import Chalice

from chalicelib.challenge import Challenge
from chalicelib.challenge_email import ChallengeEmail
from chalicelib.utils import get_df_from_s3, read_s3_file

app = Chalice(app_name='stori')


@app.on_s3_event(bucket=os.getenv('BUCKET'),
                 events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    """
    Handles an S3 event.

    This function is triggered when a new object is created in the specified S3 bucket.
    It reads the object, which is expected to be a CSV file, into a DataFrame.
    Then it creates a Challenge object from the DataFrame and sends an email about the challenge.

    Parameters
    ----------
    event : chalice.app.S3Event
        The S3 event that triggered the function.

    Returns
    -------
    dict
        A dictionary with a greeting and the total balance of the challenge.
    """
    challenge = Challenge(df=get_df_from_s3(event.bucket, event.key))
    ChallengeEmail.send_email(challenge, csv_bytes=read_s3_file(event.bucket, event.key).read().decode('utf-8'))
