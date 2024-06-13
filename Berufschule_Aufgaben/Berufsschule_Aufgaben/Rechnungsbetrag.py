import re

text = "The quick brown fox jumps over the lazy dog"

treffer = re.compile("The quick brown", text)
if treffer:
    print("Treffer gefunden!")
    print("Startindex des Treffers:", treffer.start())
    print("Endindex des Treffers:", treffer.end())
    print("Gefundener Text:", treffer.group())
else:
    print("Kein Treffer gefunden.")
