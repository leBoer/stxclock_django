from django.contrib import admin

from .models import Exchange, Weekend, Holiday

admin.site.register(Exchange)
admin.site.register(Weekend)
admin.site.register(Holiday)
