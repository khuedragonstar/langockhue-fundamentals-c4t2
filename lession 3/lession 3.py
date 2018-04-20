# bai 1
# for i in range (2000, 3200):  # trong khoang
#     if i%7 ==0 and i%5 !=0:   # x%y==z x chia y dư z
#         print()               # != khác

#bài no name no1
# for x in range (1,35):
#     y = 35-x
#     a= y*4+x*2
#     if a == 94:
#         print(x)
#         print(y)
# he phuong trinh bac 1 ,2 an tong quat
a = int(input("nhap he so cua pt1:"))
b = int(input("nhap he so cua pt1:"))
c = int(input("nhap he so cua pt2:"))
d = int(input("nhap he so cua pt2:"))
e = int(input("nhap ket qua pt1:"))
f = int(input("nhap ket qua pt2:"))
print("phuong trinh he 2 an bac 1")
print("he phuong trinh la: {0}x + {1}y = {2}".format(a,b,e))
print("he phuong trinh la: {0}x + {1}y = {2}".format(c,d,f))
d = a*d - b*c
dx = e*d - b*f
dy = a*f - e*c
if d == 0 and dx == 0:
    print("he vo so nghiem")
if d == 0 and dx != 0:
    print("he vo nghiem")
if d != 0:
    print("he co nghiem")
    print("x =",d/dx)
    print("y =",d/dy)
# bai no name no2
#n = int(input("nhap so n:"))
# cach 1
# f = 1
# if n >= 0:
#     for i in range (n):
#         f = f +100
#     print(f)
# else:
#     print("n ko lon hon 0")
# cach 2
# a= 1 + 100*n
# print(a)
# cach 3
# def f(n):
#     if n == 0:
#         return 1
#     else:
#         return f(n-1) +100
# print (f(n))


