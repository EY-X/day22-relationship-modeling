from django.contrib import admin
from author_book.models import *

admin.site.register(Chapter)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Author)
admin.site.register(AuthorBook)
admin.site.register(BookReader)
