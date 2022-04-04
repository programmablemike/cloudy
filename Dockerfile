FROM alpine:latest
WORKDIR /app
# Install packages
RUN apk update && apk add build-base python3-dev gcc g++
# Create a Python virtualenv
RUN python3 -m venv virtualenv
# Copy the requirements file
COPY requirements.txt .
RUN . ./virtualenv/bin/activate && pip install -r requirements.txt
# Copy the application files
COPY . .
ENV FLASK_APP=/app/app.py
EXPOSE 5000
CMD . ./virtualenv/bin/activate && flask run -h 0.0.0.0 -p 5000