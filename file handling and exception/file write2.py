# 2 method: writeline
file = open("first.txt","w")
data = ["Congratulations to all of you","disha\n", "abhay\n"]
file.write(data)
print("data written successfully")
file.close()