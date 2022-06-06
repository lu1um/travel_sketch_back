from django.contrib import admin
from .models import *


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(News)
admin.site.register(Region)
admin.site.register(Tag)