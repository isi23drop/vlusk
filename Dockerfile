FROM python:3.13-rc-alpine3.18

WORKDIR /usr/src/app/
COPY ./requirements.txt .
RUN python -m pip install --no-cache-dir -r /app/requirements.txt

COPY . .
CMD [ "python", "./your-daemon-or-script.py" ]
