file = open(r'C:\Users\lenovo\Desktop\PYTHON(INTERNSHIP)\Assignments\Day 13\sowpods.txt')
words = file.readlines()
words = [w.strip() for w in words]
file.close()