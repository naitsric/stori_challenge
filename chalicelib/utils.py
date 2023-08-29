from email import encoders
from email.mime.base import MIMEBase

import boto3
import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_s3_file(bucket: str, key: str) -> bytes:
    """
    Reads a file from an S3 bucket.

    Parameters
    ----------
    bucket : str
        The name of the S3 bucket.
    key : str
        The key of the file in the S3 bucket.

    Returns
    -------
    bytes
        The content of the file as bytes.
    """
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, key)

    return obj.get()['Body']


def get_df(_bytes: bytes) -> DataFrame | TextFileReader:
    """
    Converts bytes to a Pandas DataFrame.

    Parameters
    ----------
    _bytes : bytes
        The bytes to be converted.

    Returns
    -------
    DataFrame | TextFileReader
        The resulting DataFrame.
    """
    return pd.read_csv(_bytes)


def get_df_from_s3(bucket: str, key: str) -> DataFrame | TextFileReader:
    """
    Reads a CSV file from an S3 bucket and converts it to a DataFrame.

    Parameters
    ----------
    bucket : str
        The name of the S3 bucket.
    key : str
        The key of the file in the S3 bucket.

    Returns
    -------
    DataFrame | TextFileReader
        The resulting DataFrame.
    """
    _bytes = read_s3_file(bucket, key)
    return get_df(_bytes)


def send_email(
        subject: str, body: str, to: str, smtp_server: str,
        smtp_port: int, smtp_user: str, smtp_password: str,
        csv_bytes: bytes = None):
    """
    Sends an email with an optional CSV attachment.

    Parameters
    ----------
    subject : str
        The subject of the email.
    body : str
        The body of the email.
    to : str
        The recipient of the email.
    smtp_server : str
        The SMTP server to use to send the email.
    smtp_port : int
        The port to use on the SMTP server.
    smtp_user : str
        The username to use to login to the SMTP server.
    smtp_password : str
        The password to use to login to the SMTP server.
    csv_bytes : bytes, optional
        The CSV file to attach to the email, by default None
    """
    msg = MIMEMultipart()

    msg['From'] = smtp_user
    msg['To'] = to
    msg['Subject'] = subject

    if csv_bytes:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(csv_bytes)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="file.csv"')
        msg.attach(part)

    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(msg)
    server.quit()
