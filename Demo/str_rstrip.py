"""
เมธอด rstrip () ใช้สำหรับตัดช่องว่างหรือตัวอักขระทางด้านหลังของสตริง
"""
str1 = "___Python programming___"
"""  
rstrip("_") ตัดสตริงด้านหลัง
lstrip("_") ตัดสตริงด้านหน้า
strip("_") ตัดสตริงทั้งด้านหน้าด้านหลัง
"""
str_r1 = str1.rstrip("_")
str_r2 = str1.lstrip("_")
str_r3 = str1.strip("_")
print(str_r3)

