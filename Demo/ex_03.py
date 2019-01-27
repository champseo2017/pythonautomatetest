input_name = input("Enter name : ")
input_address = input("Enter Address : ")
input_zipcode = input("Enter Zipcode : ")
#เมธอด ljust() ใช้สำหรับจัดสตริงให้ชิดซ้ายตามจำนวนความยาวที่กำหนด str.ljust(width,"ตัวอักขระที่ต้องการแทนช่องว่าง") (ตัวอักขระที่ต้องการแทนช่องว่าง) กำหนดหรือไม่ก็ได้
input_to_name = input("Enter Name to : ")
input_to_address = input("Enter Address to : ")
input_to_zipcode = input("Enter Zipcode to : ")
# เมธอด center() ใช้สำหรับจัดสตริงให้อยู่ตรงกลาง str.center(width,"ตัวอักขระที่ต้องการแทนช่องว่าง")(ตัวอักขระที่ต้องการแทนช่องว่าง) กำหนดหรือไม่ก็ได้
print("From \n" + input_name.ljust(20,"_") + "\n"
      + input_address.ljust(20,"_") + "\n"
      + input_zipcode.ljust(20,"_") + "\n" +
      "To".rjust(25) + "\n" + input_to_name.ljust(20,"_").center(72) + "\n" +
      input_to_address.ljust(20,"_").center(72) + "\n" +
      input_to_zipcode.ljust(20,"_").center(72))