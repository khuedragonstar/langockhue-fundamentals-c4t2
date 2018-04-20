# là 1 dãy giá trị ko thay đổi immmuteable

# ko the thay doi tuple, no la duy nhat, la phep them bot phan tu chi la tao lai 1 tuple khac
a=(1,2,3)
b=(1,2)
print(hex(id(a)))#dia chi 1
a = a+b
print(a)
print(hex(id(a)))#dia chi sau khi tao lai 1 tuple khac
print("array")
#mang co the them bot phan tu ma ko thay doi vung bo nho
c = [1,2,3]
print(hex(id(c)))
c.append([1,2])
print(c)
print(hex(id(c)))