"""
เพิ่มลบแก้ไข lsit และ dictionary and tuple
รายการแบบ dictionary สามารถทำได้แค่ แก้ไขและลบข้อมูลเท่านั้นไม่สามารถเพิ่มได้
"""
ls = [10, 2.25, 'python']
ls = ls + ['ggwp'] #เพิ่มข้อมูล list index + ค่าที่จะเพิ่ม
ls[3] = 45 #แก้ไขข้อมูล list index = ค่าที่จะแก้ไข
del ls[3] #คำสั่งลบ ตัวแปร index ที่จะลบ
print(ls)

std = {'stdId': 25, 'stdName': 'John', 'stdSubj': ['math', 'Science', 'Computer']}
std['stdSubj'][0] = 'Peter' #แก้ไข
del std['stdSubj'][0] #ลบ
print(std)

"""
ตรวจสอบชนิดข้อมูล type
"""
int = 3
float = 8.8
string = 'ggwp'
ls = [10, 45, 60]
die = {'a': 1, 'b': 2, 'c': 3}
tup =('a', 'b', 8)
print(type(int))
print(type(float))
print(type(string))
print(type(ls))
print(type(die))
print(type(tup))


