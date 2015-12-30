for denDigOne in range(1,10):
    for denDigTwo in range(10):
        denominator = int(str(denDigOne)+str(denDigTwo))
        for numDigOne in range(1,10):
            for numDigTwo in range(10):
                numerator = int(str(numDigOne)+str(numDigTwo))
                quotient = numerator/denominator
                if denominator <= numerator or (numDigTwo == 0 and denDigTwo == 0):
                    continue
                if denDigOne == numDigOne and denDigTwo != 0:
                    if (numDigTwo/denDigTwo) == quotient:
                        print(numDigOne,numDigTwo,"/",denDigOne,denDigTwo)
                if denDigOne == numDigTwo and denDigTwo != 0:
                    if (numDigOne/denDigTwo) == quotient:
                        print(numDigOne,numDigTwo,"/",denDigOne,denDigTwo)
                if denDigTwo == numDigOne and denDigOne != 0:
                    if (numDigTwo/denDigOne) == quotient:
                        print(numDigOne,numDigTwo,"/",denDigOne,denDigTwo)
                if denDigTwo == numDigTwo and denDigOne != 0:
                    if (numDigOne/denDigOne) == quotient:
                        print(numDigOne,numDigTwo,"/",denDigOne,denDigTwo)
