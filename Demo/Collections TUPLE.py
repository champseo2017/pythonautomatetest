my_tuple = ("Apples", "Oranges", "Grapes")

print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:2])

for val in my_tuple:
    print(val)
print(len(my_tuple))
my_tuple_2 = ("Banana", (1,2,3), ["Tokyo", "New Delhi"])
print(my_tuple_2[2][1])

my_tuple_2[2][1] = "New York"
print(my_tuple_2)

print("Banana" in my_tuple_2) # True
print("Cherry" in my_tuple_2) # False

test = 23; test2 = "แมว"
print("แมว %s \n\t\
    - ทดสอบครั้งที่ 1 = %d " %(test2, test))

print("สมใจ เรียนวิชา {} ได้คะแนน\n\
      ทดสอบครั้งที่ 1 = {:.2f}" .format("system", 30.56))