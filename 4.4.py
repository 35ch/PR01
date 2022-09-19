bensinpris = float(input("Vad är det nuvarande bensinpriset? (kr/l) "))

if bensinpris < 10:
    print("Det var billigt!")

elif bensinpris <= 15:
    print("Tanka full tank.")

elif bensinpris <= 20:
    print("Tanka tio liter")

elif bensinpris > 20:
    print("Nu säljer jag bilen och cyklar istället.")
