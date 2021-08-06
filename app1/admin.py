from django.contrib import admin
from .models import Posts

admin.site.site_header='ADMIN'
admin.site.site_title='WELCOME ADMIN'
admin.site.index_title='OVERVIEW'

admin.site.register(Posts)
