from celery import Celery

import time
import random

# Create the celery app for the workers
app = Celery(
    'src',
    broker='redis://localhost',
    backend='redis://localhost',
    include=['src.worker.tasks']
)
