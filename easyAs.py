def checkDigits(num):
    digits=str(num)
    if digits[0]=='1':
        if digits[2]=='2':
            if digits[4]=='3':
                if digits[6]=='4':
                    if digits[8]=='5':
                        if digits[10]=='6':
                            if digits[12]=='7':
                                if digits[14]=='8':
                                    if digits[16]=='9':
                                        if digits[18]=='0':
                                            return True
    return False

i=1010101010
#for i in range(1010101010,1390000000,10):
while True:
    i+=10
    if checkDigits(i*i):
        print str(i)
        print(i*i)
        break
