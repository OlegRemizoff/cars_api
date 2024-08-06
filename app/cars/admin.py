from django.contrib import admin
from cars.models import Auto, ModelAuto


class ModelAutoAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]


class AutoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "model", "year", "mileage", "price", "fuel", "transmission"]
    list_display_links = ["id", "name"]



admin.site.register(Auto, AutoAdmin)
admin.site.register(ModelAuto, ModelAutoAdmin)
