# 1) თითოეულ მეთოდზე: len, append, insert, pop, remove მეთოდებზე გააკეთეთ 3-3 მაგალითი. len ფუნქციაზე მოიყვანეთ string-ის მაგალითიც
# len ფუნქცია
my_list = [1, 2, 3, 4]
print(len(my_list))  

names = ["Ana", "Gio", "Nino"]
print(len(names))  

text = "Hello World"
print(len(text))  

# append
nums = [1, 2, 3]
nums.append(4)
print(nums)  

fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  

letters = []
letters.append("a")
letters.append("b")
print(letters) 

# insert
colors = ["red", "blue"]
colors.insert(1, "green")
print(colors)  

numbers = [10, 30]
numbers.insert(1, 20)
print(numbers) 

items = ["a", "c"]
items.insert(1, "b")
print(items)  

# pop
nums = [1, 2, 3]
x = nums.pop()
print(x)      
print(nums)   

letters = ["a", "b", "c"]
letters.pop(1)
print(letters)  

words = ["hello", "world"]
removed = words.pop(0)
print(removed)  
print(words)   

# remove
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)  

fruits = ["apple", "banana", "apple"]
fruits.remove("apple")
print(fruits) 

chars = ["x", "y", "z"]
chars.remove("y")
print(chars)  















