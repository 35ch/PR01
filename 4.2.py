vikt, längd = map(float, input("Ange din vikt (kg) och längd (cm) separerat av ett mellanslag: ").split())

längd /= 100

bmi = vikt/längd**2

if bmi < 18.5:
    print("Du har undervikt.")

elif bmi >= 18.5 and bmi < 25:
    print("Du har normalvikt.")

elif bmi >= 25 and bmi < 30:
    print("Du har övervikt.")

elif bmi > 30:
    print("Du har tyvärr fetma.")

