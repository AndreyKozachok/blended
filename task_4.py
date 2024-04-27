# У Джо Палуки товсті пальці, тому він завжди натискає клавішу "Caps Lock", коли насправді має намір натиснути клавішу "a". 
# (Коли Джо намагається ввести якусь акцентовану версію "a", яка потребує більше натискань клавіш для створення акцентів, 
#  він більш обережний у присутності таких рафінованих символів ([Shift] + [a]) і буде натискати клавіші правильно). 
# Обчисліть і виведіть результат введення Джо заданого тексту. Клавіша "Caps Lock" впливає лише на клавіші з літерами від "a" до "z", 
# і не впливає на інші клавіші або символи. вважається, що клавіша "Caps Lock" спочатку вимкнена.

def caps_lock(text):
    # result = ""
    # up = False
    # for letter in text:
    #     if letter != "a":
    #         result += letter if up == False else letter.upper()
    #     else:
    #         up = not up
    # print(result)
    # return result
    pis_text = text.split("a")
    print(pis_text)
    for i in range(1, len(pis_text), 2):
        pis_text[i]= pis_text[i].upper()
    result = ''.join(pis_text)
    print(result)
    return result


assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"

