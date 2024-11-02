# read file
f = open("demo.txt", "r")
data = f.read()
read_with_size = f.read(5)
line1 = f.readline()
line2 = f.readline()
print(data)
print(read_with_size)
print(line1)
print(line2)
f.close()

append_file = open("demo.txt", "a")
user_inputted_text = input("write something you want to add in the demo file: ")
append_file.write(user_inputted_text)

append_file.close()
