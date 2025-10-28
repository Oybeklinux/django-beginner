from django.contrib import admin
from .models import Profil, Skill
# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']

admin.site.register(Profil)
admin.site.register(Skill, SkillAdmin)