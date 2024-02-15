import logging
from time import sleep

import requests
from celery.result import AsyncResult

from tasks.celery import app

logger = logging.getLogger('main')


@app.task(bind=False, retry_backoff=True, queue='tasks')
def sending_request(command: str) -> None:
    '''Отправляет запрос во второй микросервис.'''

    try:
        response = requests.post(
            'http://creating-queue:8000/api/processing_command/',
            data={'command': command},
        )
        if response.status_code == 200:
            check_status.delay(response.json()['task_id'], command)
        else:
            logger.error(f'Ошибка {response.status_code}')
    except Exception:
        logger.error('Ошибка при отправлении задачи во второй микросервис!')


@app.task(bind=False, retry_backoff=True, queue='tasks')
def check_status(task_id: str, command: str) -> None:
    '''Проверяет очередь, подтверждает выполнение команды.'''

    result = AsyncResult(task_id)
    while result.status != 'SUCCESS':
        result = AsyncResult(task_id)
        sleep(10)
    logger.info(f'Команда `{command}` успешно выполнена!')
