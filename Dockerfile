# pull official base image
FROM python:3.12-alpine
WORKDIR /app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
COPY ./ssl/johnshelby.crt .
COPY ./ssl/johnshelby.key .
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"] 
# "runserver_plus", "--cert-file", "johnshelby.crt","--key-file", "johnshelby.key",