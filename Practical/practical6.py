# Write a Python program to find the first appearance of the substring 'not' and'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

msg=input("Enter the string: ")
msg1=msg
if msg.find("not poor")!=-1:
    #pos=msg.find("not poor")
    msg1=msg.replace("not poor","good")


print(msg1)
