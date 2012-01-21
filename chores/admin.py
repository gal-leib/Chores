from chores.models import Chore, CompletedChore
from django.contrib import admin

class ChoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'reward')

admin.site.register(Chore, ChoreAdmin)
admin.site.register(CompletedChore)
