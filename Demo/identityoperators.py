"""
ตัวดำเนินการเอกลักษณ์ตรวจสอบว่าข้อมูลที่อยู่ในตัวแปรหรืออ๊อบเจ็คมีค่าเหมือนกันหรือไม่เหมือนกัน
is  = True ถ้าค่าในตัวแปร A และ B มีค่าเหือนกัน
is not = True ถ้าค่าในตัวแปร A และ B มีค่าไม่เหมือนกัน
"""
x = 12 - 6
y = 3 * 2

e_x = x is y
print(e_x)

ex_is_not = 13 is not y
print(ex_is_not)

key = input('Enter a key: ')
print(key is 'y')

