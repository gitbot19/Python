citirus_fruits = ['mango','lemon']
fruits = ['grape', 'orange', 'banana', 'grape', 'kiwi']


basket = list()

for fruit in range(len(fruits)):
    print(fruits[fruit])
    if fruits[fruit] not in basket:
        basket.append(fruits[fruit])


print('basket of fruits')
print(basket)