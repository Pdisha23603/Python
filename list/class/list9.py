# to display ascending order
# lst_number=[1,2,3,4,5,6,7,8,8]
# lst_city=["ahmedabad","rajkot","surat","amereli"]
# print(f"original list {lst_number} - {lst_city}")
# lst_number.sort()
# lst_city.sort()
# print(f"after sort {lst_number} - {lst_city}")




# to display decending order
lst_number=[1,2,3,4,5,6,7,8,8]
lst_city=["ahmedabad","rajkot","surat","amereli"]
print(f"original list {lst_number} - {lst_city}")
lst_number.sort(reverse=True)
lst_city.sort(reverse=True)
print(f"after sort {lst_number} - {lst_city}")


# sort cities according 
lst_city.sort(key=len)
print(f"after sorting accoriding len {lst_city}")