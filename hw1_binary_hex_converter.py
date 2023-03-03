while True:
    inputnumber = input("Please type the number between 0 to 255 : ")
    number = int(inputnumber)

    if number < 0 :
        print("The number you type is negative. Try again! The number you type is: ", number)
    elif number <= 255:
        print("Correct! The number you type is : ", number)
        break
    else:
        print("The numbner you type is bigger than 255. Try again! The number you type is : ", number)


# Binary
# 2 ** 8
if number < 256 :
    bi_8 = 0
else:
    number = number - 256
    bi_8 = 1

# 2 ** 7
if number < 128 :
    bi_7 = 0
else:
    number = number - 128
    bi_7 = 1

# 2 ** 6
if number < 64:
    bi_6 = 0
else:
    number = number - 64
    bi_6 = 1

# 2 ** 5
if number < 32:
    bi_5 = 0
else:
    number = number - 32
    bi_5 = 1

# 2 ** 4
if number < 16:
    bi_4 = 0
else:
    number = number - 16
    bi_4 =1

# 2 ** 3
if number < 8:
    bi_3 = 0
else:
    number = number - 8
    bi_3 = 1

# 2 ** 2
if number < 4:
    bi_2 = 0
else:
    number = number - 4
    bi_2 = 1

# 2 ** 1
if number < 2:
    bi_1 = 0
else:
    number = number - 2
    bi_1 = 1

# 2**0
if number < 1:
    bi_0 = 0
else:
    number = number - 1
    bi_0 = 1

print("輸入10進位: " , inputnumber, "，等於2進位: "  , bi_8, bi_7, bi_6, bi_5, bi_4, bi_3, bi_2, bi_1, bi_0)





#Hexadecimal_Right

r_total = bi_3*8 + bi_2*4 + bi_1*2+bi_0*1

l_total = bi_7*8 + bi_6*4 + bi_5*2+bi_4*1


if r_total == 10:
    r_total = "A"
elif r_total == 11:
    r_total = "B"
elif r_total == 12:
    r_total ="C"
elif r_total == 13:
    r_total = "D"
elif r_total == 14:
    r_total = "E"
elif r_total == 15:
    r_total = "F"



if l_total == 10:
    l_total = "A"
elif l_total == 11:
    l_total = "B"
elif l_total == 12:
    l_total ="C"
elif l_total == 13:
    l_total = "D"
elif l_total == 14:
    l_total = "E"
elif l_total == 15:
    l_total = "F"


print("輸入10進位: " , inputnumber, "，等於16進位: "  , l_total, r_total)





    