"""
เมธอด replace () ใช้สำหรับแทนที่่ข้อความ
"""
str1 = "python is programming language, python is programming language"
str_rep = str1.replace("python", "Python")
str_rep1 = str1.replace("python", "Python", 2)
print("ข้อความเดิม =", str1)
print("ข้อความใหม่ replace แบบปกติไม่ใส่จำนวนรอบในการ replace =", str_rep)
print("ข้อความใหม่ replace แบบใส่จำนวนรอบในการเปลียน = ", str_rep1)
