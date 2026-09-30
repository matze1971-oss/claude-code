"""Speichert das Mail-Passwort in der Windows-Anmeldeinformationsverwaltung.

Aufruf: python passwort_speichern.py name@anbieter.de
Das Passwort wird verdeckt abgefragt und landet nie in einer Datei.
"""

import getpass
import sys

import keyring

if len(sys.argv) != 2:
    sys.exit("Aufruf: python passwort_speichern.py name@anbieter.de")

benutzer = sys.argv[1]
pw = getpass.getpass(f"Passwort für {benutzer}: ")
if not pw:
    sys.exit("Kein Passwort eingegeben, nichts gespeichert.")
keyring.set_password("superhirn-mail", benutzer, pw)
print("Gespeichert. Zu finden unter Systemsteuerung > Anmeldeinformationsverwaltung > superhirn-mail.")
