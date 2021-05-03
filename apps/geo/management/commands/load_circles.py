from django.core.management.base import BaseCommand, CommandError
from geo.models import Geo
import xlrd

class Command(BaseCommand):
    help = 'Load regions'

    def handle(self, *args, **options):
        workbook = xlrd.open_workbook(r'/code/apps/geo/Cercles.xlsx')
        sheet = workbook.sheet_by_index(0)
        for r in range(1, sheet.nrows):
            name = sheet.cell(r,0).value
            type = sheet.cell(r,1).value
            lon = sheet.cell(r,2).value
            lat = sheet.cell(r,3).value

            nb_hbts = sheet.cell(r,4).value
            area = sheet.cell(r,5).value
            manager = sheet.cell(r,6).value
            parent = sheet.cell(r,7).value
 
            self.stdout.write(self.style.SUCCESS('Loading circle : %s'%name ))
            try:
                geo = Geo.objects.get(name = name,type = "CERCLE")
            except Geo.DoesNotExist as e:
                try:
                    geo = Geo()
                    geo.name = name
                    geo.type = type
                    geo.lon = lon
                    geo.lat = lat
                    geo.nb_hbts = nb_hbts
                    geo.area = area
                    geo.manager = manager
                    geo.parent = Geo.objects.get(name = parent,type="REGION")
                    geo.save()
                except Exception as e:
                    self.stdout.write(self.style.ERROR('Error when loading  circle : %s'%name ))

        
