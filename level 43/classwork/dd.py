#  1.შექმენი dictionary, სადაც იქნება სტუდენტის სახელი, ასაკი და ქულა. შემდეგ დაბეჭდე მხოლოდ ქულა.

student = {
    "name": "Nika",
    "age": 16,
    "score": 95
}

print(student["score"])

# 2.შექმენი dictionary მანქანის შესახებ და დაამატე ახალი მნიშვნელობა "color".

car = {
    "brand": "Toyota",
    "model": "Corolla"
}

car["color"] = "Black"

print(car)

# 3.შექმენი dictionary და შეცვალე ერთ-ერთი მნიშვნელობა.
person = {
    "name": "Ana",
    "age": 20
}

person["age"] = 21

print(person)


# 4.ექმენი dictionary 3 ხილით, მიუწერეთ მათი ფერები და for ციკლით დაბეჭდე ყველა key და value.

fruits = {
    "apple": "red",
    "banana": "yellow",
    "kiwi": "green"
}

for key, value in fruits.items():
    print(key, "-", value)


# 5.ქვევით მოცემულ dictonary-ში დაამატე კიდევ ერთი პროდუქტი (dict-ში ჩაშენებული dict) სახელად "headphones", რომელსაც ექნება მნიშვნელობები: price → 400 / stock → 12 / rating → 4.8


store = {
    "laptop": {
        "price": 3200,
        "stock": 5,
        "rating": 4.7
    },
    "phone": {
        "price": 1800,
        "stock": 8,
        "rating": 4.5
    },
    "tablet": {
        "price": 1200,
        "stock": 3,
        "rating": 4.2
    }
}

store["headphones"] = {
    "price": 400,
    "stock": 12,
    "rating": 4.8
}

print(store)


# 6.უკვე შექმნილ dictionary-ში ყველა პროდუქტის ფასი გაზარდეთ 10%-ით (* 1.1)
for product in store:
    store[product]["price"] *= 1.1

print(store)


# 7.უკვე შექმნილი dictionary-ს გამოყენებით შექმენით ახალი dictionary სახელად high_rated სადაც შეინახავთ ისეთ პროდუქტებს, რომლის rating > 4.5-ზე


high_rated = {}

for product, info in store.items():
    if info["rating"] > 4.5:
        high_rated[product] = info

print(high_rated)