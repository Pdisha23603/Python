name = input("enter name: ")
part1 = name[0:2]
part2 = name[2:(len(name)-2)]
part3 = name[(len(name)-2):]
ans = part3 + part2 + part1
print(ans)