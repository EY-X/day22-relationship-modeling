from django.contrib import admin
from worker_shift.models import *


admin.site.register(Shift)
admin.site.register(Worker)
admin.site.register(WorkerShift)