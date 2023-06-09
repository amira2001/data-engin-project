FROM python:latest
COPY . . 
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y cron
RUN touch /var/log/cron.log
RUN echo "* * * * * root /cron_script.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/cron_job
RUN chmod 0644 /etc/cron.d/cron_job
CMD cron && tail -f /var/log/cron.log


