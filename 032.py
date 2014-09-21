"""Notes:

"""

def checkProducts(numString,products):
    length = len(numString)
    numString = ''.join(numString)
    for i in range(1,length - 2):
        for j in range(i+1,length):
            product = int(numString[j:length])
            if int(numString[0:i]) * int(numString[i:j]) == product:
                products.add(product)
                print(''.join(numString[0:i]) + ' * ' + ''.join(numString[i:j]) + ' = ' + ''.join(numString[j:len(numString)]))

products = set([])
digit1 = [1,2,3,4,5,6,7,8,9]
#print(digit1)
for a in digit1:
    digit2=list(digit1)
    digit2.remove(a)
    for b in digit2:
        digit3=list(digit2)
        digit3.remove(b)
        for c in digit3:
            digit4=list(digit3)
            digit4.remove(c)
            for d in digit4:
                digit5=list(digit4)
                digit5.remove(d)
                for e in digit5:
                    digit6=list(digit5)
                    digit6.remove(e)
                    for f in digit6:
                        digit7 = list(digit6)
                        digit7.remove(f)
                        for g in digit7:
                            digit8 = list(digit7)
                            digit8.remove(g)
                            for h in digit8:
                                digit9 = list(digit8)
                                digit9.remove(h)
                                for i in digit9:
                                    numString = [str(a),str(b),str(c),str(d),str(e),str(f),str(g),str(h),str(i)]
                                    checkProducts(numString,products)
                                    break
checkProducts(str(123456789),products)
print(sum(products))