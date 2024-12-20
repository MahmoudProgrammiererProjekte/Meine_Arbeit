from django.db import models  

class Video(models.Model):
    title = models.CharField(max_length=200)  
    # Speichert den Titel des Videos (max. 200 Zeichen)

    description = models.TextField()  
    # Speichert eine längere Beschreibung ohne Längenbegrenzung

    upload_date = models.DateTimeField(auto_now_add=True)  
    # Speichert das Erstellungsdatum und die Uhrzeit (automatisch)

    category = models.CharField(max_length=100, blank=True, null=True)  
    # Optional: Speichert die Kategorie des Videos (z. B. "Lernen")

    views = models.PositiveIntegerField(default=0)  
    # Speichert die Anzahl der Aufrufe (nur positive Zahlen, Standard=0)

    def __str__(self):
        return self.title  
        # Gibt den Titel des Videos zurück, wenn das Objekt dargestellt wird
