from core.tasks import sending_request
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Отправить задачу во второй микросервис'

    def add_arguments(self, parser):
        parser.add_argument('command', nargs='?', type=str)

    def handle(self, *args, **options):
        if not options['command']:
            self.stdout.write(self.style.ERROR('Отсутствует задача!'))
        else:
            sending_request.delay(options['command'])
