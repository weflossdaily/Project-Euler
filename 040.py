def numDigits(number):
    if number < 10:
        return 1
    if number < 100:
        return 2
    if number < 1000:
        return 3
    if number < 10000:
        return 4
    if number < 100000:
        return 5
    return 6

product=1
place=1
nextPlace = place*10
for i in range(2,1000000):
    length = numDigits(i)
    if place + length >= nextPlace:
        # print('place: ' + str(place) + ', i: '+ str(i) +', length: ' + str(length) +', product: ' + str(product) + ', nextPlace: ' + str(nextPlace) +', impotant digit: '+str(i)[nextPlace-place-1] )
        product *= int(str(i)[nextPlace-place-1])
        nextPlace*=10
    place += length
print(product)
