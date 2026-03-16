# writting mode
file = open("first.txt","w")
data = "Congratulations to all of you"
file.write(data)
file.close()

# append 
file = open("first.txt","a")
data = "Congratulations to all of you"
file.write(data)
file.close()