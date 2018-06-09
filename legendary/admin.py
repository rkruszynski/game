from django.contrib import admin

from .models import Hero, Team, Scheme, Mastermind, Villians

# Register your models here.
admin.site.register(Hero)
admin.site.register(Team)
admin.site.register(Scheme)
admin.site.register(Mastermind)
admin.site.register(Villians)