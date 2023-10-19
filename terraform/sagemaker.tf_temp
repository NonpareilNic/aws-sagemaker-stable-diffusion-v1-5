resource "aws_sagemaker_endpoint_configuration" "config" {
  name = "massdriver-inference-endpoint-config"

  production_variants {
    variant_name           = "massdriver-variant-0"
    model_name             = aws_sagemaker_model.sdxl_model.name
    initial_instance_count = 1
    instance_type          = "ml.t2.medium"
  }

  tags = {
    Name = "NicTesting"
  }
}


resource "aws_sagemaker_endpoint" "sdxl_endpoint" {
  name   = "massdriver_sdxl_endpoint"
  endpoint_config_name = aws_sagemaker_endpoint_configuration.config.name
}

resource "aws_sagemaker_model" "sdxl_model" {
  name               = "massdriver-sdxl"
  execution_role_arn = aws_iam_role.sagemaker_admin.arn

  primary_container {
    image = "763104351884.dkr.ecr.us-west-2.amazonaws.com/huggingface-pytorch-inference:1.7.1-transformers4.6.1-gpu-py36-cu110-ubuntu18.04"
    model_data = "s3://${aws_s3_bucket.dkneipp_sagemaker.bucket}/model.tar.gz"
  }
}

data "aws_sagemaker_prebuilt_ecr_image" "test" {
  repository_name = "kmeans"
}

/*
from sagemaker.huggingface.model import HuggingFaceModel

import conf

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(**conf.MODEL_PARAMS)

# deploy the endpoint endpoint
predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.g4dn.xlarge",
    endpoint_name=conf.RESOURCE_NAME,
)

*/