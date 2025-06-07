FROM python:3.10-slim

WORKDIR /app

COPY ../requirements/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ../ ./

RUN apt-get update && apt-get install -y supervisor

COPY ./Docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8000 
EXPOSE 8501 

CMD ["/usr/bin/supervisord"]