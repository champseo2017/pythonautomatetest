"""
การแปลงชนิดข้อมูล
"""
int_01 = '9'
con_int = int(int_01)
check_type_int = type(con_int)
print(con_int)

float_02 = 9.9
con_float = int(float_02)
chack_type_float = type(con_float)
print(con_float)

str_01 = 25
con_str = str(str_01)
check_type_str = type(con_str)
print(str_01)

list_to_set = [1,2,3]
con_list_to_set = set(list_to_set)
check_type_con_list = type(con_list_to_set)
print(con_list_to_set)

set_to_tuple = {'a':1, 'b':2, 'c':3}
con_set_to_tuple = tuple(set_to_tuple)
check_type_con_set_tuple = type(con_set_to_tuple)
print(con_set_to_tuple)

tuple_to_set = (1,2,3,4,5,6)
con_tuple_to_set = set(tuple_to_set)
check_type_con_tuple = type(con_tuple_to_set)
print(con_tuple_to_set)

list_to_dict = [[1,2], [3,4]]
con_list_to_dict = dict(list_to_dict)
check_type_listdict = type(con_list_to_dict)
print(con_list_to_dict)

"""
ใช้ตัวแปรเดิมแต่เป็นชนิดข้อมูลใหม่ได้
สามารถนำตัวแปรกับมาใช้ใหม่ได้
"""
list_to_dict = (1,2,3,4,5,6)
con_list_to_dict = list(list_to_dict)
print(con_list_to_dict)