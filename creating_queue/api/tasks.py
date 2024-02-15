from creating_queue.celery import app


@app.task(bind=False, retry_backoff=True, queue='creating-queue')
def processing_command_task(command: str) -> None:
    '''Обработка полученной задачи.'''

    pass
