from django.contrib import admin
from library_book.models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Patron)
admin.site.register(Loan)
admin.site.register(Hold)