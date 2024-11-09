from celery import Celery

app = Celery("beat-worker", backend="redis://localhost:6379/0", broker="amqp://guest@localhost:5672//")
