def calculation(sym, m, n):
    if sym == '/':
        try:
            n = m / n
            return n
        except ZeroDivisionError:
            print('Can\'t divide by Zero!')
            # print('Zero Division Error!')
            return 0


    elif sym == '*':
        n = m * n
        return n
         
    elif sym == '+':
        n = m + n
        return n
       
    elif sym == '-':
        n = m - n
        return n
    
    else:
        print('Invalid Operator!')
        return 0

if __name__ == "__main__":
    CStack = []                             #calculation stack
    DStack = []                             #display stack
    
    operand1 = input('Enter first operand: ')
    if operand1 == '=':
        print('Exit!')
        
    else:
        CStack.append(float(operand1))
        m = CStack[0]
        DStack.append(CStack[0])

        while True:
            operator = input('Enter an operator: ')
            
            if operator == '=':
                print('Result =',str(CStack[0]))
                break
        
            elif operand1.lower() == 'c':
                print('Clear')

            else:
                CStack.append(operator)
                operand2 = input('Enter second operand: ')
                if operand2 == '=':
                    print('Result =',str(CStack[0]))
                    break

                # elif operand1.lower() == 'x':
                #     print('Exit!')

                else:
                    CStack.append(float(operand2))

                    for element in CStack[1:]:
                            DStack.append(element)

                # reverse all the values in DStack from top to bottom
                # CStack.reverse()
                # m = CStack[-1]
                sym = CStack[1]
                n = CStack[2]

                res = calculation(sym, m, n)
                CStack[0] = m = res 

                CStack.pop(-2)
                CStack.pop(-1)
                
            Final = ' '.join(map(str, DStack))
            print(f'{Final} = {res}')


            # Final = ' '
            # for x in DStack:
            #     Final += ' '+ str(x)
            # print(f'{Final} = {res}')


            # Final = ' '.join(str(item) for item in DStack)
            # print(f'{Final} = {res}')