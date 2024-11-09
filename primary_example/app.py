from celery import Celery
import random

app = Celery("beat-worker", backend="redis://localhost:6379/0", broker="amqp://guest@localhost:5672//", include="tasks")
app.conf.beat_schedule = {
    'add-random': {
        'task': 'tasks.add',
        'schedule': 5.0,
        'args': (random.randint(0,10), random.randint(0,20))
    },
    'log-uptime': {
        'task': 'tasks.log_uptime',
        'schedule': 10.0,
        'args': ('uptime.log',)
    }
}