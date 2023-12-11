def welcome_teacher(name):
    greeting = f"Вітаю, вчителю {name}!"
    return greeting

teacher_name = ("Криворучик Дмитро")
welcome_message = welcome_teacher(teacher_name)
print(welcome_message)