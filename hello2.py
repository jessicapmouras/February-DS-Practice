lst = [(50000, 0.08), (100000, 0.10), (150000, 0.15)]

lst2 = [(10000, 0.02), (20000, 0.08)]

def calc_taxes(lst, income):
  #counter for total taxes
  total_taxes = 0

  #iterate over each tuple in list
  for max_tax, tax_rate in lst:

    if income <= max_tax:
      total_taxes += income * tax_rate
      income = (income - max_tax)
      break
    else:
      total_taxes += max_tax * tax_rate
      income = (income - max_tax)
      

  if income <= 0:
    total_taxes = total_taxes
  else:
    total_taxes + (income * tax_rate)

  return total_taxes
print(calc_taxes(lst, 70000))
print(calc_taxes(lst2, 30000))