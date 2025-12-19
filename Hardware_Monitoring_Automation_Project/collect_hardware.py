# Importiert psutil für Hardware- und Systeminformationen
import psutil  

# Importiert sqlite3 für die Arbeit mit einer SQLite-Datenbank
import sqlite3  

# Importiert datetime, um Zeitstempel zu speichern
from datetime import datetime  

# Verbindet sich mit der Datenbank (wird erstellt, falls sie nicht existiert)
connection = sqlite3.connect("hardware.db")  

# Erstellt einen Cursor, um SQL-Befehle auszuführen
cursor = connection.cursor()  

# Erstellt eine Tabelle für Hardware-Daten, falls sie noch nicht existiert
cursor.execute("""
CREATE TABLE IF NOT EXISTS hardware_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpu_cores INTEGER,
    ram_gb REAL,
    disk_gb REAL,
    timestamp TEXT
)
""")  

# Liest die Anzahl der CPU-Kerne aus
cpu_cores = psutil.cpu_count(logical=True)  

# Liest den gesamten Arbeitsspeicher (RAM) in Bytes
ram_bytes = psutil.virtual_memory().total  

# Konvertiert RAM von Bytes in Gigabyte
ram_gb = round(ram_bytes / (1024 ** 3), 2)  

# Liest den gesamten Speicherplatz der Festplatte
disk_bytes = psutil.disk_usage("/").total  

# Konvertiert Festplattenspeicher von Bytes in Gigabyte
disk_gb = round(disk_bytes / (1024 ** 3), 2)  

# Erstellt einen Zeitstempel für den aktuellen Zeitpunkt
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

# Fügt die gesammelten Hardware-Daten in die Datenbank ein
cursor.execute("""
INSERT INTO hardware_info (cpu_cores, ram_gb, disk_gb, timestamp)
VALUES (?, ?, ?, ?)
""", (cpu_cores, ram_gb, disk_gb, timestamp))  

# Speichert die Änderungen dauerhaft in der Datenbank
connection.commit()  

# Gibt die gesammelten Informationen in der Konsole aus
print("Hardware-Daten erfolgreich gespeichert:")  

# Gibt die CPU-Kerne aus
print(f"CPU Kerne: {cpu_cores}")  

# Gibt den RAM in GB aus
print(f"RAM (GB): {ram_gb}")  

# Gibt den Festplattenspeicher in GB aus
print(f"Festplatte (GB): {disk_gb}")  

# Gibt den Zeitstempel aus
print(f"Zeitpunkt: {timestamp}")  

# Schließt die Verbindung zur Datenbank
connection.close()  
