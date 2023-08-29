import boto3
import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_s3_file(bucket: str, key: str) -> bytes:
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, key)

    return obj.get()['Body']


def get_df(_bytes: bytes) -> DataFrame | TextFileReader:
    return pd.read_csv(_bytes)


def get_df_from_s3(bucket: str, key: str) -> DataFrame | TextFileReader:
    _bytes = read_s3_file(bucket, key)
    return get_df(_bytes)


def send_email(subject, body, to, smtp_server, smtp_port, smtp_user, smtp_password):
    msg = MIMEMultipart()

    msg['From'] = smtp_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(msg)
    server.quit()
