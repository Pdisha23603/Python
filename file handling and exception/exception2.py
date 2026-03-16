# import traceback
# try:
#     data = {"name":"disha"}
#     num = int(input("enter number: "))
# except:
#     print("IN EXCEPT BLOCK")
#     traceback.print_exc()
#     # traceback.format_exc()
#     print(traceback.format_exc())

# import traceback
# try:
#     data = {"name":"disha"}
#     num = int(input("enter number: "))
#     print(data["age"])
# except Exception as e:
#     print("IN EXCEPT BLOCK")
#     traceback.print_exc()
#     # traceback.format_exc()
#     print(traceback.format_exc())
#     print(e)



import traceback
try:
    data = {"name":"disha"}
    num = int(input("enter number: "))
    print(data["age"])
except ValueError as e: #ValueError is a class
    print(e)