from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from web_app.models import TProcedures
from web_app.service import get_data_from_xml


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('xml_file', type=str)

    def handle(self, *args, **options):
        xml_file = options['xml_file']
        try:
            with open(xml_file, 'rb') as fobj:
                xml = fobj.read()
        except IOError:
            self.stderr.write(self.style.ERROR('File "%s" not found' % xml_file))

        dic = get_data_from_xml(xml)
        t_procedure = TProcedures(**dic)
        t_procedure.save()
        self.stdout.write(self.style.SUCCESS('Successfully import xml file "%s"' % xml_file))
