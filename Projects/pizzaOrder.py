def func(name, address, **orders):
    print(f'This order is for {name}')
    print(f'ship to {address}')

    price = 40
    # here we will traverse for each, for each order 50 rs will be added to the delivery charges
    for food in orders.values():
        # check if food is ordered or not
        if(food):
            price += 50
    print(f'The total price is {price}')
    return price


func('rohit', 'shanti nivas, thane', chinese = True, chikenHandi = True, roti = True, colddrink = True, rice = False)