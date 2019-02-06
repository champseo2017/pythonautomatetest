n = input('Please enter Integer number : ')
# แจ้งให้ป้อนเลขจำนวนเต็มเก็บไว้ใน n
n = int (n) # แปลงค่าใน n เป็นจำนวนเต็ม
if n > 0: # กำหนดเงื่อนไขหลัก ถ้าค่า n มากกว่าศูนย์จะเป็นจำนวนเต็มบวก
    if n%2 == 0: # กำหนดเงื่อนไขย่อย ตรวจสอบว่าเป็นเลขคู่ หรือเลขคี่
        print("Positive even number")
    else:
        print("Positive odd number")
elif n == 0: # กำหนดเงื่อนไขหลักถ้าค่า n เท่ากับศูนย์
    print("Zero number")
else: # กำหนดเงื่อนไขหลักถ้า n คือค่าลบ -9
    print("Negative number")