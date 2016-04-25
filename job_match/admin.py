from django.contrib import admin
from models import Writer, Publication

admin.site.register([Writer, Publication])
