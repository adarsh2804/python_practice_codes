
f = open('myfile_read', 'r')  # it is opened in the read mode
# print(f.readline(), end='')   # readline has pointer on the next line which is first line in this case
# print(f.readline(), end='')   # end is given to not give next line
# print(f.read())               # will read the entire file

f1 = open('myfile_write', 'w')  # opened in write mode, will overwrite the content in the file everytime
# f1.write("Something")

# f2 = open('myfile_write', 'a')           # opened in append mode, will append the data in the file not overwrite
# f2.write('is there')

for data in f:         # will read the data from file f
    f1.write(data)        # write the data in f1
