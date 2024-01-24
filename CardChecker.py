print('Enter the sixteen digits of the card: \n')
cardNumber = []
for i in range(0,16):
    i = int(input(f'{i+1} Digit: '))
    cardNumber.append(i)
    pass
oddTotal = 0
greaterThan4 = 0
for i in range(0, 15, 2):
    oddTotal += cardNumber[i]
    if(cardNumber[i]> 4):
        greaterThan4 += 1
        pass
    pass
oddTotal *= 2
evenTotal = 0
for i in range(1, 15, 2):
    evenTotal += cardNumber[i]
    pass
finalTotal = oddTotal+evenTotal+greaterThan4
lastDigit = finalTotal % 10
checkDigit = 10 - lastDigit
if(cardNumber[15]==checkDigit):
    print(f"The Check Digit matches the Last Digit.\nHence, the Card Number is valid.")
    pass
else:
    print("Invalid Card Number")


