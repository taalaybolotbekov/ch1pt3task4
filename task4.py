def palin():
    slovo = str(input('Введите слово: '))
    a = slovo[::-1]
    if slovo == a:
        return True 
    else:
        return False
print(palin())