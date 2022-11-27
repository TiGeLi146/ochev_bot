# Очистка имени пользователя от тегов
def clear_firstname(firstname):
    if "<" in firstname: firstname = firstname.replace("<", "*")
    if ">" in firstname: firstname = firstname.replace(">", "*")
    return firstname


