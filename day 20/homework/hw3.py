# 5) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები
correct_pin="8901"
attempts=3
while attempts >0:
    pin=input("enter your pin:")
    if pin ==correct_pin:
        print("Access granted:")
        break
    else:
        attempts-=1
        print("incorect pin")
        if attempts ==0:
            print("Access Denied:")
        