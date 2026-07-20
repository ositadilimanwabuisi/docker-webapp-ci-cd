# start with python base image
FROM python:3.12-slim

#set who built this image
LABEL maintainer="ositadilimanwabuisi(at)gmail.com"

# set working directory
WORKDIR /app

#copy our app into the container
COPY app.py .

# Tell Docker which port our app uses
EXPOSE 8080

#run the app when container starts
CMD ["python3", "app.py"]
