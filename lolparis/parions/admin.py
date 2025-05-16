from django.contrib import admin

# Register your models here.

from .models import Match, Pari

admin.site.register(Match)
admin.site.register(Pari)