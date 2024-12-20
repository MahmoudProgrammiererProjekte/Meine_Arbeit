from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'upload_date', 'category', 'views')
    # Diese Felder werden in der Admin-Übersicht angezeigt

    list_filter = ('upload_date', 'category')  
    # Ermöglicht das Filtern nach Datum und Kategorie

    search_fields = ('title', 'description')  
    # Ermöglicht die Suche nach Titel und Beschreibung
