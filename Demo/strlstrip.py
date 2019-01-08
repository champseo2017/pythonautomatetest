"""
เมธอด lstrip () ใช้สำหรับลบช่องว่าง หรือตัวอักขระทางด้านหน้าของสตริง
"""
str1 = "____Python programming___"
str2 = "   Python programming    "
str_1 = str1.lstrip("_")
str_2 = str2.lstrip(" ")
print(str_1)
print(str_2)