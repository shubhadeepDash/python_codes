file2 = open(r'C:\Users\lenovo\Desktop\PYTHON(INTERNSHIP)\Assignments\Day 13\sonnet_words.txt')
words2 = file2.readlines()
words2 = [w.strip() for w in words2] 
file2.close()