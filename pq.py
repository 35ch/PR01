p, q = map(float, input("Please provide the value of p and q separated by a space: ").split())

d = (p/2) ** 2 - q 
# Diskriminanten

# Om diskriminanten är negativ har ekvationen inga lösningar
if d < 0:
    print("This equation has no real roots!")

# Om diskriminanten är lika med noll så har x1 och x2 samma värde
elif d == 0:
    x = -p/2
    print(f"x={-p/2 + d**(1/2)}")

# Om diskrinanten är större än ett får x1 och x2 olika värden
elif d > 0:
    x1 = -p/2 + d**(1/2)
    x2 = -p/2 - d**(1/2)
    print(f"x1={x1}, x2={x2}")


