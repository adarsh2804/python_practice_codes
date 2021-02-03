f = open('MY_IMG_READ.JPG', 'rb')

f1 = open('MY_IMG_WRITE.JPG', 'wb')

for i in f:
    f1.write(i)
