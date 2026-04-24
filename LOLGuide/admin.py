from django.contrib import admin # type: ignore
from .models import Champion, Ability, Item, Region, JungleMonsters, Profile

admin.site.register(Profile)

class AbilityInline(admin.TabularInline):
    model = Ability
    extra = 5

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'tagline', 'color')
    search_fields = ('name', 'tagline')

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'role', 'region')
    search_fields = ('name',)

    inlines = [AbilityInline]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'stat_display')
    search_fields = ('name',)

@admin.register(JungleMonsters)
class JungleMonsterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

