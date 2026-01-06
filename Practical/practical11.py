# Write a Python program to unzip a list of tuples into individual lists.

data = [("frans","paris"),("india","delhi"),("germany","berlin")]
lst_country, lst_capital = zip(*data)
print(lst_country)
print(lst_capital) 