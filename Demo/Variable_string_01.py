# การกำหนดชนิดข้อมูลสตริง
# สตริง ( String ) เป็นการนำอักขระแต่ล่ะตัวมาวางเรียงต่อกันให้กลายเป็นข้อความ ซึ้งเราต้องกำหนดจุดเริ่มต้นและสิ้นสุดของมันด้วยเครื่องหมาย Double Quotes ("")
# หรือไม่ก็ใช้ Single Quote ('')
title = "Python Programming"
hbd = 'Happy Birthday'
hny = "สวัสดี ปีใหม่"
longText = \
    "สตริง เป็นการนำอักขระแต่ล่ะตัวมาวางเรียงต่อกันให้กลายเป็นข้อความ"
# about_python = "python is a high-level, interpretd, interactive
# and object-orieented programming language" #Error
about_python = "Python is a hight-level, interpreted, interactive \
and object - oriented programming language" #ขึ้นบรรทัดใหม่ string ใช้ \เลื่อนค่าไปไว้ที่บรรทัดถัดไป # ok
count =\
'one,\
Two,\
Three,\
Four'

#หากแยกบรรทัดแล้วเเยื้อง string จะเกิดช่องว่างระหว่างสตริงเท่ากับระยะที่เยี้อง

count_2 = \
'one, \
Two, \
Three, \
Four'

# สำหรับการกำหนด string ด้วยเครื่องหมาย "" หรือ '' ตามปกติเราสามารถเลือกใช้อันไดก็ได้
# ซึ้งบางครั้งอาจใช้ร่วมกัน ถ้าใน string นั้นมี " เป็นส่วนหนึ่งของมันด้วย เราก็ครอบสตริงทั้งหมด (ข้างนอก)
# ด้วย '' หรือในทางตรงกันข้าม ' ครอบด้วย "" (ข้างนอก)

#message = 'Let \'s go' #Error เพราะใช้เครื่องหมาย ' ซ้อนกัน (\คั่นหน้า " หรือ ' เพื่อที่เราจะได้ไม่ต้องครอบด้วย " หรือ ' สลับไปมา)
message = "Let 's go" #ok
# text = "She said \"Hello World!\"" # Error เพราะใช้เครื่องหมาย " ซ้อนกัน  (\คั่นหน้า " หรือ ' เพื่อที่เราจะได้ไม่ต้องครอบด้วย " หรือ ' สลับไปมา)
text = 'She said "Hello World!"' # ok
print(text)
# สำหรับปัญหา " หรือ ' ครอบเราสามารถแก้ไขโดยใช้ \คั่นหน้า " หรือ ' เพื่อที่เราจะได้ไม่ต้องครอบด้วย " หรือ ' สลับไปมา