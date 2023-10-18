FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

WORKDIR /app

ADD stable-diffusion-v1-5 /app/stable-diffusion-v1-5
ADD local/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD local/serving.py /app/serving.py

CMD [ "python", "serving.py" ]
