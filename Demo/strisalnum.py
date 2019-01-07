"""
เมธอด isalnum() ใช้สำหรับตรวจสอบสตริง ถ้าสตริงประกอบด้วยตัวเลขเพียงอย่างเดียว ผลลัพธ์จะเป็นจริง
แต่ถ้ามีสัญลักษณ์อื่นๆ รวมถึงช่องว่างในสตริง ผลลัพพธ์ที่ได้จะเป็น false
"""
str1 = "Python361"
str2 = "Python3.6.1 very well!!"
str3 = "Python!!!"
print("str1 =", str1.isalnum())
print("str2 =", str2.isalnum())
print("str3 =", str3.isalnum())