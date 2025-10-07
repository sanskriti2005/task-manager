# lightweigh image with python
FROM python:3.11-slim

# 
WORKDIR /backend/app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy application
COPY ./app ./app

# expose port aka, define the port in which your backend will run
EXPOSE 8000

# run FastAPI with uvicorn server 
# this is being done in the docker-compose file now
# CMD ["uvicorn", "app.main:app", "--host","0.0.0.0","--port","8000", "--reload"]