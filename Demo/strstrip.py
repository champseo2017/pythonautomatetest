"""
เมธอด strip() ใช้สำหรับลบข้อความหรือตัวอักขระและช่องว่าง ทั้งด้านหน้าและด้านหลังสตริง
"""
str1 = "     python is programming language____"
str2 = "     A, B, C, D, E, F________"
str3 = "  Python programming"

str_strip1 = str1.rstrip("_")
str_strip2 = str_strip1.lstrip()

str_strip3 = str2.rstrip("_")
str_strip4 = str_strip3.lstrip()

str_strip5 = str3.lstrip()

print("Strip1 = ", str_strip2)
print("Strip2 = ", str_strip4)
print("Strip3 = ", str_strip5)