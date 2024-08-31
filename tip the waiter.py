def tipCalc(b, tipPerc):
    tp = b * (0.01 * tipPerc)
    return tp

bill = int(input("Enter the bill:"))
tip = int(input("Enter the percentage:"))

total = bill + tipCalc(bill, tip)

print(f"bill : {bill}")
print(f"tip percentage : {tip}%")
print(f"total bill : {total}")