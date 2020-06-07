from random import randrange
from PIL import Image


suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
numbers = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

def random_selector(suits, numbers):
    suit = str(suits[randrange(0, 3)])
    number = str(numbers[randrange(0, 12)])
    print(number + ' of ' + suit)
    


random_selector(suits, numbers)
im = Image.open("image.jpg")