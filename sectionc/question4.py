#(II)
def count_words():
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

sentence = "python exam"
result = count_words(sentence)
print(result)  #  {'python': 1, 'exam': 1}

#(iii)

#(iv)
class Car:
     def __init__(self, brand,name, color):
        self.brand = brand
        self.color = color
        self.name=name

my_car = Car('Toyota', 'Red','TT')
print(f"Brand: {my_car.brand}, Color: {my_car.color} ,name: {my_car.name}")
