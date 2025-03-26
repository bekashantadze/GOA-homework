# შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები
temperature = 20
cloudy = True
summer = 40
raining = False
sunny = True
print(temperature < 30 and not raining)
print(cloudy and not sunny)
print(raining and sunny)
print(temperature > 10 or sunny)
print(sunny and not raining)