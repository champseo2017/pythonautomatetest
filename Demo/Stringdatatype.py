str_01 = "Python Programming"
str_01 = "Python programming"
print(str_01)
print(str_01)
num = 245
str1 = str(num)
print(str1)
print("ชนิดข้อมูลของ str1 คือ ", type(str1))
print("ชนิดข้อมูลของ num คือ", type(num))

str1 = "hello"
str2 = "Python"
str3 = "Programming"
print(str1, " ", str2, str3)
print(str1 + " " + str2 + str3)

str1 = "Python"
str2 = "Python"
print (str1 *3)
print(3 * str1)
print(3 * str2)

str1 = "Python"
str2 = "Python"
str3 = ""
str4 = " "
str5 = "อักขระหรือสตริง"
print("จำนวนอักขระใน str1 = ", len(str1))
print("จำนวนอักขระใน str2 = ", len(str2))
print("จำนวนอักขระใน str3 = ", len(str3))
print("จำนวนอักขระใน str4 = ", len(str4))
print("จำนวนอักขระใน str5 = ", len(str5))

str1 = "Hello Python"
print("จำนวนตัวอักขระทั้งหมดค ือ", len(str1))
print("ตำแหน่งที่ 0 คือ ", str1[0])
print("ตำแหน่งที่ -1 คือ ", str1[-1])
print("ตำแหน่งที่ 5 คือ ", str1[5])
print("ตำแหน่งที่ -5 คือ ", str1[-5])
print("ผลลัพธ์ที่ได้จากการตัดคำ 0:4 = ", str1[0:4])
print("ผลลัพธ์ที่ได้จากการตัดคำ -6:-1 = ", str1[-6:-1])
print("ผลลัพธ์ที่ได้จากการตัดคำ 6:12 = ", str1[6:12])
print("ผลลัพธ์ที่ได้จากการตัดคำ 0:5 = ", str1[:5])
print("ผลลัพธ์ที่ได้จากการตัดคำ = ", str1[:])
print("ผลลัพธ์ที่ได้จากการตัดคำ = ", str1[-12:-8:2]) #str[start:stop:step] ระบุการกระโดดข้ามตัวอักษรไป 2 ตำแหน่ง ( step +1 ) (start + 1)
print("ผลลัพธ์ที่ได้จากการตัดคำ = ", str1[1::2]) #str[start:stop:step] ระบุการกระโดดข้ามตัวอักษรไป 2 ตำแหน่ง ( step +1 ) (start + 1)