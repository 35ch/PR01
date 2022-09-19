årtal = int(input("Skriv ett årtal efter 1753: "))

# Årtal som ej är århundraden
if årtal % 4 == 0 and årtal % 100 != 0:
    print(f"{årtal} är ett skottår.")

# Årtal som är århundraden
elif årtal % 400 == 0:
    print(f"{årtal} är ett skottår.")

else:
    print(f"{årtal} är inte ett skottår.")

