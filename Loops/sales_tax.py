# Apply 8% sales tax

subtotals = [15.98, 899.97, 799.97, 117.96, 5.99, 599.99, 24.99, 1799.94, 99.99]

taxes = []
totals = []

for i in range(len(subtotals)):
    taxes.append(round(subtotals[i] * .08, 2))
    totals.append(round(subtotals[i] + taxes[i], 2))

print(taxes)
print(totals)

# 2nd method

# for subtotal in subtotals:
#    tax = round(subtotal * .08, 2)
#    total = round(subtotal + tax, 2)
#    taxes.append(tax)
#    totals.append(total)

# print(taxes)
# print(totals)