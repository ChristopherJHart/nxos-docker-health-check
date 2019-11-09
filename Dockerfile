FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY nxos_health_check/ /app/

CMD [ "python", "./health_check.py" ]