# 7) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს რიცხვს და დააბრუნებს მის ფაქტორიალს. n რიცხვის ფაქტოირალი არის ყველა მთელი დადებითი რიცხვის ნამრავლი 1-იდან n-ის ჩათვლით
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = 5
fact = factorial(number)
print(f"{number} რიცხვის ფაქტორიალი არის: {fact}")
