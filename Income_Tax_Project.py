#Income Tax Project

income = float(input("Enter the gross income: "))

#print(f"{income:.2f}")

numberOfDependents = int(input("Enter the number of dependents: "))

#print(numberOfDependents)

dependentsDeduction = numberOfDependents * 3000

standardDeduction = 10000

incomeTax = (income - dependentsDeduction - standardDeduction) * 0.20

if (incomeTax >= 0):
    print(f"The income tax is ${incomeTax}")
else:
    print(f"The income tax is -${abs(incomeTax)}")