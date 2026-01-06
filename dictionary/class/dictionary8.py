# store data of student : name, email, contact no, address, marks
student_data = {"disha@gmail.com":["disha","9876543210","himmatnagar",95],"abhay@gmail.com":["abhay","8765432109","ahmedabad",90],
                "kinjal@gmail.com":["kinjal","7654321098","surat",85], "krutarth@gmail.com":["krutarth","6543210987","vadodara",80]}
# items method
for i,j in student_data.items():
    # print(i,j)
    print(i)
    for i1 in j:
        # print(i1)
        print("\t",i1)
