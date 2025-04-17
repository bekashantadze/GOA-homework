# 7) მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)
sentence=input("შეიყვანე წინადადება:")
vowel_count=0
consonant_count=0
for letter in sentence:
    if letter.isalpha():
        if letter.lower() in "a e i o u":
            vowel +=1
        else:
            consoants +=1
print("vowels:",vowel_count)
print("consonants:",consonant_count)