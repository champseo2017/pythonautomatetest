str = "A     B     C     D     E     F     G     H     I     J     K     L     M     N     O     P     Q     R     S     T     U     V     W     X     Y     Z"
#การกระโดนข้ามตัวอักษร จำนวนที่จะกระโดดข้าม -1
#str[start:stop:step]
#การตัดตัวอักษรและการกระโดดข้าม
#index = -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 ตำแหน่งท้าย สุด จะเป็น -1
#Streing = H  e  l   l  o      P  y  t  h  o  n
#undex =   0  1  2  3   4   5  6  7  8  9  10 11
#รหัสพิเศษควบคุมการแสดงผลชนิดข้อมูลสตริง (Escape Sequences) "\n" ขึ้นบรรทัดใหม่
# เมธอด len(str) หาความยาวของสตริง
# เมธอด find() คืนค่ามาเป็นตำแหน่งของตัวอักษร ถ้าไม่เจอตัวอักษรที่ต้องการค้นหาจะคืนค่ามาเป็น -1
str_removespace = str.replace(" ", "") #เมธอด replace() ใช้สำหรับแทนที่ข้อความ str.replace(old, new, จำนวนตำแหน่งที่ต้องการแทนที่)
str_ex1 = str_removespace[0] + str_removespace[4] + str_removespace[8] + str_removespace[14] + str_removespace[20]
print("แสดงผลเฉพาะสระ ภาษาอังกฤษและแสดงตำแหน่งที่อยู่ของสระแต่ล่ะตัว \n",str_ex1,"\n","ตำแหน่งของสระแต่ล่ะตัว \n",
      str_ex1.find("A"),str_ex1.find("E"),str_ex1.find("I"),str_ex1.find("O"),str_ex1.find("U"))