FROM public.ecr.aws/lambda/python:3.11

# Lambda requires /var/task
WORKDIR /var/task

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy local python package
COPY bedrock_lib ./bedrock_lib
RUN pip install ./bedrock_lib

# Copy FastAPI app
COPY app ./app

# Lambda handler (NO uvicorn, NO expose)
CMD ["app.main.handler"]
