# მომხმარებელს input-ის საშვალებით შემოტანინეთ ორი რიცხვი number1 და number2 შემდეგ კი დაბეჭდეთ მათი ჯამი. ასევე შექმენით level-ის ცვლადი რომელშიც მომხამრებელს შემოაყვანინებთ მათ ამჟამინდელ level-ს, შეეცადეთ level-ის მნიშვნელობას დაუმატოთ ერთი და ისე დაბეჭდოთ. მიღებული შედეგებით გამოიტანეთ დასკვნა და დაწერეთ კომენტარებით
num_1 =int(input("choose_num1: "))
num_2= int(input("choose_num2: "))

print( num_1 + num_2 )

current_level= input( "please write maine current level: ")
print(current_level + 1)
