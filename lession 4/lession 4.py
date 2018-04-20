#class ten_class: #khai bao class
    #thuoc tinh
    #phuong thuc

#ex
class Hcn:
    width = 10  #
    height = 100#bo di ko anh huong
    def  __init__(self,w,h):
        self.width = w
        self.height = h
    def chuvi(self):
        p = (self.width + self.height)*2
        return p
# tao ra 1 doi tuong
a1 = Hcn(10,100)
a2 = Hcn(30,100)

cv1 = a1.chuvi()
print("a1 chuci:", cv1)



