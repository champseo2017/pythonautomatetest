"""
เมธอด isdecimal() ถ้าสตริงเป็นตัวเลข ผลลัพธ์ที่ได้จะเป็นจริง (True)
แต่ถ้าไม่ใช้ตัวเลขทั้งหมดผลลัพธ์จะเป็น false
"""
str1 = "322456"
str2 = "341522 python Programming"
str3 = "!!!!"
print("str1 เป็นตัวเลขทั้งหมดหรือไม่ =", str1.isdecimal())
print("str2 เป็นตัวเลขทั้งหมดหรือไม่ =", str2.isdecimal())
print("str3 เป็นตัวเลทั้งหมดหรือไม่ =", str3.isdecimal())