import os
import csv
import re
import argparse

# Argument parser initialisieren
parser = argparse.ArgumentParser(
    description="Erstellt einen HTML-Bericht aus einer CSV-Datei.")
parser.add_argument("-i", "--input", help="Pfad zur CSV-Datei", required=True)
parser.add_argument(
    "-o", "--output", help="Dateiname/Pfad des HTML-Berichts", required=True)

# Argumente parsen
args = parser.parse_args()

# Überprüfen, ob Eingabeparameter vorhanden sind
if not args.input or not args.output:
    print("Bitte geben Sie den Pfad zur CSV-Datei und den Dateinamen/den Pfad des HTML-Berichts an.")
    exit()

# Suchen nach der CSV-Datei
csv_filepath = args.input
if not os.path.isfile(csv_filepath):
    print(f"Die Datei '{csv_filepath}' wurde nicht gefunden.")
    exit()

# Suchen nach dem Ausgabepfad für den HTML-Bericht
output_filepath = args.output
if not output_filepath.endswith('.html'):
    output_filepath += '.html'

# Datenstrukturen initialisieren
metadata_list = []
profiles = []
employee_data = []

# CSV-Datei öffnen und lesen
with open(csv_filepath, 'r') as file:
    reader = csv.reader(file)
    section = None

    for row in reader:
        # Leere Zeilen überspringen
        if len(row) == 0:
            continue

        # Abschnittswechsel erkennen
        if row[0] == "project_name":
            section = "metadata"
            continue
        elif row[0] == "profile_name":
            section = "profiles"
            continue
        elif row[0] == "employee_id":
            section = "employee_data"
            continue

        # Daten je nach Abschnitt speichern
        if section == "metadata":
            metadata = {
                "Project Name": row[0],
                "Project Manager": row[1],
                "Start Date": row[2],
                "End Date": row[3]
            }
            metadata_list.append(metadata)
        elif section == "profiles":
            profiles.append(row)
        elif section == "employee_data":
            employee_data.append(row)

# Metadaten formatieren
metadata_html = ''.join(
    [f"<div class=\"card\"><strong>{key}:</strong> {value}</div>" for metadata in metadata_list for key, value in metadata.items()])

# Profile formatieren
profiles_html = ''.join(
    [f"<tr><td>{profile[0]}</td><td>{profile[1]}</td></tr>" for profile in profiles])

# Mitarbeiterdaten formatieren
employee_data_html = ''.join([f"<div class=\"card1\"><strong>Employee ID:</strong> {data[0]}</div>"
                              f"<div class=\"card1\"><strong>Name:</strong> {data[1]}</div>"
                              f"<div class=\"card1\"><strong>Position:</strong> {data[2]}</div>" for data in employee_data])

# Den relativen Pfad zur "html_report_template.html"-Datei im aktuellen Verzeichnis erstellen
template_html_path = os.path.join(
    os.path.dirname(__file__), "html_report.html")

# Öffne und lese die "html_report_template.html"-Datei
with open(template_html_path, "r") as f:
    html_content = f.read()

    # Füge zusätzliche Metadaten ein
    html_content = html_content.replace(
        "<!-- Additional Metadata will be inserted here -->", metadata_html)

    # Füge zusätzliche Profile ein
    match = re.search(
        r"(<table>\s*<tr>\s*<th>Profile Name<\/th>\s*<th>Details<\/th>\s*<\/tr>)", html_content)
    if match:
        insertion_point = match.end()
        html_content = html_content[:insertion_point] + \
            profiles_html + html_content[insertion_point:]

    # Füge zusätzliche Mitarbeiterdaten ein
    match = re.search(
        r"(<div id=\"employee_data\" class=\"employee_data\">\s*<h2>Employee Data<\/h2>)", html_content)
    if match:
        insertion_point = match.end()
        html_content = html_content[:insertion_point] + \
            employee_data_html + html_content[insertion_point:]

# HTML-Datei mit aktualisierten Metadaten, Profile und Mitarbeiterdaten speichern
with open(output_filepath, "w") as f:
    f.write(html_content)

print(f"HTML-Bericht wurde erfolgreich erstellt: {output_filepath}")
