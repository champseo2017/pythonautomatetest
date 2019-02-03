# คำสั่งหากใส่ ; ก็สามารถทำได้
# ภาษา Python จะถือว่าโค้ดในบรรทัดเดียวกัน คือคำสั่งเดียวกัน และ เมื่อขึ้นบรรทัดใหม่ก็ถือว่าเป็นคำสั่งใหม่
# and Compound Statement คือ statement ที่มีหลายคำสั่ง หรือมี statement ย่อยๆหลายอันรวมกัน
x = 0 # Single Statement คือ statement ที่มีเพียงคำสั่งเดียว
if x == 0: # Compound Statement คือ statement ที่มีหลายคำสั่ง หรือมี statement ย่อยๆหลายอันรวมกัน
    message = "Error..."
    print(message)
else:
    print("ok")
x = 10; y = 99.99; # คำสั่งหากใส่ ; ก็สามารถทำได้
z = x + y;
print(z);