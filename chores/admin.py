from chores.models import Chore, CompletedChore, Player
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ChoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'reward')

class PlayerInline(admin.StackedInline):
    model = Player

class PlayerAdmin(UserAdmin):
    inlines = [PlayerInline,]

admin.site.register(Chore, ChoreAdmin)
admin.site.register(CompletedChore)
admin.site.unregister(User)
admin.site.register(User, PlayerAdmin)
