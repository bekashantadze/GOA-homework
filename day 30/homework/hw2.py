# 4) შექმენით ფუნქცია რომელიც მიიღებს რიცხვს (int) და სიტყვას (string) პარამეტრებად, ფუნქციამ მიღებული სიტყვა უნდა დაბეჭდოს იმდენჯერ რამდენიც არის რიცხვის არგუმენტი
def repeat_word(times, word):
    for _ in range(times):
        print(word)

repeat_word(3, "Hello")

