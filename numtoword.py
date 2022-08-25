#number to word converter
#Assigment 
#Tamerat Legesse
def number_converter(number):
    numbers = {
            0:"ዜሮ",1:"አንድ",2:"ሁለት",3:"ሶስት",4:'አራት',5:'አምስት',6:'ስድስት',7:'ሰባት',8:'ስምንት',9:'ዘጠኝ',10:'አስር',11:'አስራ አንድ',\
            12:'አስራ ሁለት',13:'አስራ ሶስት',14:'አስራ አራት',15:'አስራ አምስት',16:'አስራ ስድስት',17:'አስራ ሰባት',18:'አስራ ስምንት',19:'አስራ ዘጠኝ',\
            20:'ሃያ',30:'ሰላሳ',40:'አርባ',50:'ሃምሳ',60:'ስልሳ',70:'ሰባ',80:'ሰማንያ',90:'ዘጠና'}
    if number < 20:
        return numbers[number]
    elif number < 100:
        if number % 10 == 0:
            return numbers[number]
        else:
            return numbers[number - (number % 10)] + f" {numbers[number % 10]}"
    elif number < 1000:
        if number % 100 == 0:
            return numbers[number // 100] + " መቶ"
        else:
            return numbers[number // 100] + " መቶ " + number_converter(number % 100)
    elif number < 1000000:
        if number % 1000 == 0:
            return number_converter(number // 1000) + " ሺህ"
        else:
            return number_converter(number // 1000) + " ሺህ" + f" {number_converter(number % 1000)}"
    elif number < 1000000000:
        if number % 1000000 == 0:
            return number_converter(number // 1000000) + " ሚሊዮን"
        else:
            return number_converter(number // 1000000) + " ሚሊዮን" + f" {number_converter(number % 1000000)}"
    elif number < 1000000000000:
        if number % 1000000000 == 0:
            return number_converter(number // 1000000000) + " ቢሊዮን"
        else:
            return number_converter(number // 1000000000) + " ቢሊዮን" + f" {number_converter(number % 1000000000)}"
input = input("ቁጥር አስገባ: ")
try:
    num = int(input)
    print(number_converter(num))
except:
    print("እባክዎ ትክክለኛ ቁጥር ያስገቡ እና እንደገና ይሞክሩ")