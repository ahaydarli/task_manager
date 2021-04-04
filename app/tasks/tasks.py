from core.extensions import celery
from flask import current_app
from ipdata import ipdata


@celery.task
def ip_lookup_task(ip_address):
    client = ipdata.IPData(current_app.config['IP_DATA_API_KEY'])

    return client.lookup(ip_address)
