# เมธอด copy() ใช้สำหรับคัดลอกชนิดข้อมูลลิสต์
# lst_new = lst.copy()
# โดยที่ lst_new คือ ตัวแปรเก็บข้อมูลชนิดลิสต์
# lst คือ ตัวแปรชนิดข้อมูลลิสต์ที่ถูกคัดลอก
# นิยามทำช่องว่างที่แยกกันให้ติดกัน sep=''
books_lst = ["Python", "Java", "C", "C++", "C#", "Scala"]
books_lst1 = books_lst.copy()
print("ข้อมูลที่อยู่ใน books_lst\n",books_lst,"\nข้อมูลที่อยู่ใน books_lst1 \n", books_lst1,sep='')