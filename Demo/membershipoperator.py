"""
ตัวดำเนินการสมาชิก Membership operator
เป็นตัวดำเนินการที่ใช้ตรวจสอบค่าว่าเป็นสมาชิกในรายการของตัวแปรหรือไม่ ตัวแปรชนิข้อมูล
String, List, Tuple, Set, และ Dictionary
ผลลัพธ์ที่ได้จะออกมาเป็น True หรือ Fault
A in B เป็นจริง ถ้า A เป็นสมาชิกที่อยู่ในรายการข้อมูลของ B
A not in B เป็นจริง ถ้าค่า A ไม่เป็นสมาชิกที่อยู่ในรายการข้อมูลของ B
"""
l = [1, 2, 3]
s = 'Hello'
d = {1: 'm', 2: 'a', 3: 'y', 4: 'a'}

t_in_s = 'e' in s
print(t_in_s)

n_in_l = 2 in l
print(n_in_l)

di_in_d = 'a' not in d
print(di_in_d)