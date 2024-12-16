def zeichne_weihnachtsbaum(hoehe):
    """
    Zeichnet einen Weihnachtsbaum mit einer angegebenen Höhe.
    """
    # Überprüfen, ob die Eingabe eine gültige Höhe ist
    if hoehe <= 0:
        print("Bitte eine positive Höhe eingeben.")
        return

    # Weihnachtsbaum zeichnen
    for i in range(hoehe):
        # Leerzeichen für die Mitte ausgeben
        print(" " * (hoehe - i - 1), end="")
        # Sterne ausgeben
        print("*" * (2 * i + 1))

    # Stamm zeichnen
    for _ in range(2):  # Der Stamm besteht aus zwei Zeilen
        print(" " * (hoehe - 1) + "|")

# Höhe des Weihnachtsbaums abfragen
try:
    hoehe = int(input("Bitte die Höhe des Weihnachtsbaums eingeben: "))
    zeichne_weihnachtsbaum(hoehe)
except ValueError:
    print("Bitte eine gültige Zahl eingeben.")
