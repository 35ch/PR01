# Delar upp input i tre delar variabler och ger de typen int
a, b, c = map(int, input("Skriv in poäng från tre prov separerat av mellanslag: ").split())

medel = (a+b+c)/3

print("Ditt medelvärde:", medel)

if medel > 90:
    print("Bra jobbat!")
