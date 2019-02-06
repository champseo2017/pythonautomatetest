count, sum = 1, 0 # กำหนดค่าตัวแปร count=1 และ sum=0
while count <= 5:
    sum += count # รอบแรกต้องเป็น 1 เพราะ count = 1  sum = count = sum + count = 1
    count += 1 # count + 1 + 1 +1 จนครบ 5 รอบ
    print("value of sum = ", sum)
# ถ้าไม่ใช้คำสั่งวนลูป while จะต้องเขียนโค๊ดคำสั่ง ดังนี้
count2, sum2 = 1, 0 # กำหนดค่าตัวแปร count=1 และ sum=0 เอา sum แต่ล่ะรอบเพิ่มจำนวน count เข้าไป
print("....................No loop While......................")
sum2 += count2
count2 += 1
print("Value of sum = ", sum2)

sum2 += count2
count2 += 1
print("value of sum = ", sum2)

sum2 += count2
count2 += 1
print("Value of sum = ", sum2)

sum2 += count2
count2 += 1
print("Value of sum = ", sum2)

sum2 += count2
count2 += 1
print("Value of sum = ", sum2)