#!/usr/bin/env bash
set -e

docker build -t stable-diffusion:latest .

docker run --gpus=all -v "$(pwd)/output:/app/output" stable-diffusion:latest
