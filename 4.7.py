print("Det här programmet kollar om du beviljas fakturabetalning.")

if input("Är du över 18 år gammal? (Ja/Nej) ").lower() == "nej":
    print("Du måste vara över 18 för att bli beviljad fakturabetalning.")
    exit()

if input("Har du några kredianmärkelser? (Ja/Nej) ").lower() == "ja":
    print("Du kan ej bli beviljad fakturabetalning om du har kreditanmärkelser.")
    exit()

if int(input("Vad är din årliga bruttoinkomst? (kr) ")) < 120000:
    print("Din årliga bruttoinkomst behöver vara över 120000kr.")
    exit()

else:
    print("Du är beviljad till fakturabetalning.")



