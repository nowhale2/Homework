immutable_var = 14, "srting", False
print(immutable_var)
# immutable_var[1] = 18  ###  На данной строке возникнет ошибка,
# так как тип tuple является объектом с фиксорованным значением
mutable_list = ["Dmitriy", 20, "student", False]
print(mutable_list)
mutable_list[0] = "Nikita"
mutable_list[1] = 19
mutable_list[3] = True
print(mutable_list)
