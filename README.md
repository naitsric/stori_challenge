# Stori Challenge

## Description

This project uses [Chalice](https://chalice.readthedocs.io/en/latest/) to build a serverless application on AWS. Python 3.10 is recommended for compatibility. The application listens for the creation of a file in an S3 bucket, summarizes the content of the file, and then sends an email with the summary and the file as an attachment.

## Pre-requisites

- Python 3.10
- [AWS CLI](https://aws.amazon.com/cli/) configured with proper credentials
- [Chalice](https://chalice.readthedocs.io/en/latest/)

## Environment Setup

### Python Installation

Make sure you have Python 3.10 installed. You can download it from [python.org](https://www.python.org/downloads/).

### Chalice Installation

To install Chalice, run the following command:

```bash
pip install chalice
```

### AWS CLI Configuration

If you haven't configured the AWS CLI yet, you can do so with the following command:

```bash
aws configure
```

Enter your credentials when prompted.

### Credentials Configuration in `.chalice/config.json`

In the `.chalice/config.json` file, add your AWS credentials and settings as well as environment variables needed for the SMTP server and S3 bucket configuration.

An example of what the file could look like is as follows:

```json
{
  "version": "2.0",
  "app_name": "MyChaliceAWSProject",
  "stages": {
    "dev": {
      "api_gateway_stage": "api",
      "manage_iam_role": false,
      "iam_role_arn": "arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_ROLE",
      "environment_variables": {
        "SMTP_SERVER": "your_smtp_server",
        "SMTP_PORT": "your_smtp_port",
        "SMTP_USER": "your_smtp_user",
        "SMTP_PASSWORD": "your_smtp_password",
        "BUCKET": "your_s3_bucket_name"
      }
    }
  }
}
```

Remember to replace the values for the environment variables `SMTP_SERVER`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, and `BUCKET` with your specific configuration details.

### Create an S3 Bucket

Before running the application, create an S3 bucket where files will be stored. This can be done either via the AWS console or by using AWS CLI:

```bash
aws s3 mb s3://[BUCKET_NAME]
```

## Dependency Installation

Install the project's dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Running the Project

To run the project locally, use:

```bash
chalice local
```

## Deployment

To deploy the project to AWS Lambda, execute:

```bash
chalice deploy
```

## Additional Documentation

- [Chalice Documentation](https://chalice.readthedocs.io/en/latest/)
- [AWS CLI Documentation](https://aws.amazon.com/documentation/cli/)

## Contributions

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
