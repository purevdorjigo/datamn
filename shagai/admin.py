from django.contrib import admin
from .models import Player, Team, ContestType, Contest, SoloPerformance


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    list_filter = ("country",)


class SoloPerformanceInline(admin.TabularInline):
    model = SoloPerformance


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "team")
    list_filter = ("team",)
    inlines = (SoloPerformanceInline,)


class ContestTypeAdmin(admin.ModelAdmin):
    pass


class ContestAdmin(admin.ModelAdmin):
    list_display = ("type", "year")
    list_filter = (
        "type",
        "year",
    )


class SoloPerformanceAdmin(admin.ModelAdmin):
    """
    Хувын цувааны админ интерфейс
    """

    list_display = (
        "contest",
        "player",
        "sum8",
        "sum4",
        "tulaa",
        "score",
        "total",
    )
    list_filter = ("contest",)


admin.site.register(ContestType, ContestTypeAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(SoloPerformance, SoloPerformanceAdmin)
