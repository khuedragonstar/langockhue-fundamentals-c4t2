# # tuoi = int(input("age?????????"))   #em chua 18
# #
# # if tuoi<14:
# #     print("baby")
# # elif 18>tuoi>=14:
# #     print("teen")
# # else:
# #     print("adult")
# ####################################################################
# a = int(input("nhap so cua x^2:")) #tinh phuong trinh bac 2
# b = int(input("nhap so cua x:"))
# c = int(input("nhap so cua:"))
# d = b**2 - 4*a*c
# x1 = (-b + d**(1/2))/2/a
# x2 = (-b - d**(1/2))/2/a
# if a == 0:
#     print ("thang nhap lieu ngu lone")
# else:
#     if d<0:
#         print("vo nghiem")
#     else:
#         if x1 == x2:
#             print("phuong trinh co nghiem kep")
#             print(x1)
#         else:
#             print("phuong trinh co 2 nghiem phan biet")
#             print (x1)
#             print (x2)
#####################################################################
# a =[]#khai bao mang
# b =[1,4,5]#khai bao va khoi tao mang
#
# for i in range (100):
#     a.append(i)
# #cach 1
# for i in b:
#     print(i,end=" ")
#cach 2 phuong phap chi so
# print(end='\n')  #cau lenh de cach dong
# for i in range (len(b)):
#     print(b[i])

#mang chua dc nhieu loai du lieu khac nhau
# c = ["tuan",1, {1,2}]
# for i in c:
#     print (i)
####bt tren lop 1
# d=[4,5,25,20,9]
# e=sum(d) #sum la ham tinh tong
# print(e)
# ###bt tren lop 2
# f=max(d)
# print (f)
# e=min(d)
# print(e)
# ###bt tren lop 1.1
# sum = 0             #
# for i in d:         #
#     sum = sum + i   # ham "sum" thuat toan
# print("sum:",sum)   #
# ###bt tren lop 2.1
# max_value = -1000     #
# for i in d:           #
#     if i > max_value: #
#         max_value = i # ham max min thuat toan
# print(max_value)      #
# ###bt tren lop 2.2    #
# min_value = 1000      #
# for i in d:           #
#     if i < min_value: #
#         min_value = i #
# print(min_value)      #
#### mang con va goi cong thuc tu file khac
##cach 1 goi de cho ez
# import sums_function as sb
# g=[1,2,5]
# h=[3,6,7,8,9]
# tongg = sb.tinhtong(g)
# tongh = sb.tinhtong(h)
# print (tongg)
# print (tongh)
#khai bao ham con
#   #from sums_function import *
