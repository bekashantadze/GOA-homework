# 10) მოცემული სიაა: ["georgia", "aRMENIA", "greeCE"]. ყველა ელემენტს ჯერ გაუკეთეთ lower, შემდეგ capitalize და დაბეჭდეთ
countries = ["georgia", "aRMENIA", "greeCE"]

for country in countries:
    formatted = country.lower().capitalize()
    print(formatted)
