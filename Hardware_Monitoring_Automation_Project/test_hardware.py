import os
import sqlite3
import subprocess
import psutil

# Test 1: Führt collect_hardware.py aus
def test_script_runs():
    result = subprocess.run(
        ["python", "collect_hardware.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0

# Test 2: Prüft, ob die Datenbank existiert
def test_database_exists():
    assert os.path.exists("hardware.db")

# Test 3: Prüft, ob Tabelle hardware_info existiert
def test_table_exists():
    conn = sqlite3.connect("hardware.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name='hardware_info'
    """)

    table = cursor.fetchone()
    conn.close()

    assert table is not None

# Test 4: Prüft, ob mindestens ein Datensatz existiert
def test_data_inserted():
    conn = sqlite3.connect("hardware.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM hardware_info")
    count = cursor.fetchone()[0]

    conn.close()
    assert count > 0

# Test 5: Prüft, ob Hardware-Werte sinnvoll sind
def test_hardware_values():
    assert psutil.cpu_count() > 0
    assert psutil.virtual_memory().total > 0
