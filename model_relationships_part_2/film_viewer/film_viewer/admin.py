from django.contrib import admin
from film_viewer.models import *


admin.site.register(Film)
admin.site.register(Viewer)
admin.site.register(FilmViewer)

