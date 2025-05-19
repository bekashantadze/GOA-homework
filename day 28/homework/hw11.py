# 13) შექმენით სტრინგი და შემოიტანეთ საძიებელი სიტყვა input-ით. თუ სიტყვა მოიძებნება find-ით, დაბეჭდეთ პოზიცია, სხვა შემთხვევაში კი დაბეჭდეთ word not found
text = "I love learning Python programming"
word = input("შეიყვანეთ საძიებელი სიტყვა: ")

position = text.find(word)

if position != -1:
    print("პოზიცია:", position)
else:
    print("word not found")
