-HTML-Berichtsgenerator
......................

Dieses Projekt erstellt einen HTML-Bericht aus einer CSV-Datei. Der Bericht enthält drei Hauptabschnitte: Metadaten, Profile und Mitarbeiterdaten. Die CSV-Datei wird analysiert und die Daten werden dynamisch in eine vorgegebene HTML-Vorlage eingefügt.

.......................

- Funktionsweise
Das Skript app.py liest die Daten aus einer angegebenen CSV-Datei, formatiert diese und fügt sie in eine HTML-Vorlage (html_report.html) ein. Der generierte HTML-Bericht enthält strukturierte Informationen zu Projekten, Profilen und Mitarbeitern.
.......................

- Anforderungen
Python 3.x
Eine CSV-Datei mit den erforderlichen Daten
Eine HTML-Vorlagendatei
.......................

- Installation

Klonen Sie das Repository oder laden Sie die Dateien herunter.
Stellen Sie sicher, dass Python 3.x installiert ist.
Speichern Sie Ihre CSV-Datei (z.B. data.csv) im gleichen Verzeichnis wie das Skript app.py.
........................

Verwendung
Platzieren Sie die HTML-Vorlagendatei (html_report.html) im selben Verzeichnis wie das Skript app.py.

Stellen Sie sicher, dass die CSV-Datei im folgenden Format vorliegt:
l
-i oder --input: Pfad zur Eingabe-CSV-Datei.
-o oder --output: Dateiname oder Pfad für den generierten HTML-Bericht.
Der HTML-Bericht wird im angegebenen Pfad (output.html) erstellt.

hier ist ein Beispiel wie ich  das Python Skript ausführen kann:

& "C:/Program Files/Python310/python.exe"  C:/Practice/Arbeit_Projekte/Report_Mitarbeiter/app.py --input C:\Practice\Arbeit_Projekte\Report_Mitarbeiter\data.csv --output  C:\Practice\Arbeit_Projekte\Report_Mitarbeiter\_Neuerstellt_html_report

#################################################################