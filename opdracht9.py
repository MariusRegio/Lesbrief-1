i = 0
maxNumber = 0
while i < 5:
    userNumber = int(input("Voer een getal boven de 0 in "))
    if userNumber > 0 and userNumber > maxNumber:
        maxNumber = userNumber
    i += 1

print("Het hoogst ingevoerde getal was", maxNumber)
