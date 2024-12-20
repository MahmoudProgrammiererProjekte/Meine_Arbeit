import re


# Ich will das hier in einer Liste:
# 536
# .h
# 14
# 10
# unused static function 'BrsHwUnlockInitInline'

warnungstext = "testtttttttttttttttttttttttt'"
variable_ctc = re.compile("ctc W(\d+): \[\'(.*)\' (\d+)\/(\d+)\] (.*)")
print(variable_ctc.findall(warnungstext))

##############################################################################################
bsp_text = "Hallo! Ich bin xMahmoudx und xJohanx versucht mir mit x100000x Beispielen Python Beizubringen."
bsp_text = "ctc W asdkgboegfbiwngioaenhrogfwergf123413625789 Fehlermeldung: 'Testfehler' Hallo! Ich bin xMahmoudx ujnd xlkshdfilab Fehler gefunden in Zeile 0:Zeichen Nummer 39745390245 nlireabgileahrgiluaergfx versucht mir mit x1091823640891264061283648926497126389464230000x Beispielen Python Beizubringen.x"

variable = re.compile("x([A-Z]?[a-z]*[[0-9]+[a-z]]*)x")
variable = re.compile(
    "ctc W.*Fehlermeldung: '(.*)'.*Zeile ([0-9]+):Zeichen Nummer ([0-9]+)")
#####################################################################################################

print(variable.findall(bsp_text))

# Ich will das hier in einer Liste:
# 536
# PrjCfg\Int\Stubs\src\BrsHw.h
# 14
# 10
# unused static function 'BrsHwUnlockInitInline'

warnungstext = "Testtttttttttttttttt'"

variable_ctc = re.compile("ctc W")
print(variable_ctc.findall(warnungstext))

# print(variable.findall(bsp_text))

# "Hallo! Ich bin xMahmoudx und xDanielx versucht mir mit x100000x Beispielen Python Beizubringen."
# "x([A-Z]?[a-z]*[0-9]*)x"


# Regex:
# ?  -->  0 oder 1 mal
# BSP: [A-Z]?  --> Finde entweder 1 Großbuchstaben oder KEINEN Großbuchstaben
# variable = re.compile("[A-Z]?")
# print(variable.findall(bsp_text))

# HAAAALLoooo   -->   Findet: H
# HAAaalloooo   -->   Findet: H
# Haaaalloooo   -->   Findet: H
# haaaalloooo   -->   Findet nichts ABER sucht danach weiter

# +  -->  1 oder 9999999999999999999999 mal
# BSP: [A-Z]+   --> Finde MINDESTENS 1 Großbuchstaben
# HAAAALLoooo   -->   Findet: HAAAALL
# HAAaalloooo   -->   Findet: HAA
# Haaaalloooo   -->   Findet: H
# haaaalloooo   -->   Findet nichts UND STOPPT DIE SUCHE

# *  -->  0 oder 9999999999999999999999 mal
# BSP: [A-Z]*   --> Finde 0 Großbuchstaben bis unendlich
# HAAAALLoooo   -->   Findet: HAAAALL
# HAAaalloooo   -->   Findet: HAA
# Haaaalloooo   -->   Findet: H
# haaaalloooo   -->   Findet nichts ABER sucht danach weiter

# ^ alles nach dem dach wird nicht angezeigt
#  BSP [^a-z]  ----> (Mahmoud 224 ? ist super) ---> es wird [ M, 224 ,?] angezeigt
