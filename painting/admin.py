from django.contrib import admin

from .models import Painting


class PaintingAdmin(admin.ModelAdmin):
    save_as = True


admin.site.register(Painting, PaintingAdmin)
