from huggingface_hub import hf_hub_download
import boto3

this_repo_id = "stabilityai/stable-diffusion-xl-base-1.0"
this_filename="sdxl-1_0.tar.gz"
this_profile_name="md-sandbox"
this_bucket_name="massdriver-diffusion-models"

aws_session = boto3.Session(profile_name=this_profile_name)
s3_client = aws_session.client('s3')

def hf_download(repo_id, filename):
    hf_hub_download(repo_id, filename)
    return filename

def upload(filename, bucket_name):
    
    with open(filename, 'rb') as data:
        s3_client.upload_fileobj(data, bucket_name, filename)

hf_download(this_repo_id, this_filename)
upload(this_filename, this)