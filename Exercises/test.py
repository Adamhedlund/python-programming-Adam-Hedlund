a = int(input("Skriv in den första vinkeln på din triangel: "))
b = int(input("Skriv in den andra vinkeln på din triangel: "))
c = int(input("Skriv in den tredje vinkeln på din triangel: "))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("Godkänd triangel!")
else:
    print("Fel input!")
if a == 90 or b == 90 or c == 90:
    print("Triangeln är rätvinklig!")
else:
    print("Triangeln är ej rätvinklig!")