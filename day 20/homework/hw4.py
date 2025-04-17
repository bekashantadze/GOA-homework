# 6) მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშუალო
total=0
count=0
while True:
    number=int(input("enter a number:"))
    if number== -1:
        break
    total +=number
    count +=1
    if count >0:
        average=total /count
        print("average:",average)
    else:
        print("no number were entered")