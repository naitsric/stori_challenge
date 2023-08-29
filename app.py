import os

from chalice import Chalice

from chalicelib.challenge import Challenge
from chalicelib.challenge_email import ChallengeEmail
from chalicelib.utils import get_df_from_s3, read_s3_file

app = Chalice(app_name='stori')


@app.on_s3_event(bucket=os.getenv('BUCKET'),
                 events=['s3:ObjectCreated:*'])
def handle_s3_event(event):

    challenge = Challenge(df=get_df_from_s3(event.bucket, event.key))
    ChallengeEmail.send_email(challenge, csv_bytes=read_s3_file(event.bucket, event.key).read().decode('utf-8'))

    return {'hello': f'world {challenge.total_balance()}'}

