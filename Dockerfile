FROM public.ecr.aws/lambda/python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy local python package
COPY bedrock_lib ./bedrock_lib
RUN pip install ./bedrock_lib

# Copy FastAPI app
COPY app ./app

EXPOSE 8000
CMD ["app.main.handler"]
