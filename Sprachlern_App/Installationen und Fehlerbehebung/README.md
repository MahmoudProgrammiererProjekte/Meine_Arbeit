---
####### Installationen und Fehler – Einrichtung von Whisper ##################################

____________________________________________________________________________________________________________________________________________
Anleitung

1. Python 3.10 installieren

Whisper funktioniert nicht mit der neuesten Python-Version. Installiere Python 3.10:
1. Lade Python 3.10 von https://www.python.org/ herunter.
2. Aktiviere während der Installation die Option: “Add Python to PATH”.

Überprüfe die Python-Version nach der Installation:

python --version

2. Virtuelle Umgebung erstellen und aktivieren

Erstelle eine virtuelle Umgebung, um Abhängigkeiten zu isolieren:

python -m venv venv

Aktiviere die virtuelle Umgebung:
• Windows:

venv\Scripts\activate


• Mac/Linux:

source venv/bin/activate

3. Whisper und Abhängigkeiten installieren
1. Whisper installieren:

pip install git+https://github.com/openai/whisper.git


2. Torch installieren (kompatible Version für Whisper):

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

4. FFmpeg installieren
1. Chocolatey installieren (nur Windows):
Öffne PowerShell als Administrator und führe folgenden Befehl aus:

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))


2. FFmpeg installieren:

choco install ffmpeg -y


3. FFmpeg überprüfen:

ffmpeg -version

5. Whisper testen

Führe Whisper aus, um eine Datei zu transkribieren:

python -m whisper <Pfad_zur_Datei> --language en --model base

Beispiel:

python -m whisper media/videos/sample.mp4 --language en --model base

###############################################################################################################################################################################################################