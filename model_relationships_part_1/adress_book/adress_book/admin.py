from django.contrib import admin
from adress_book.models import *

admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Residence)
admin.site.register(Person)

