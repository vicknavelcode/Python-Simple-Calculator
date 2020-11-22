height=float(input(' Enter Your Height '))
unit=input(' Is your height in CM or M ? ')
if unit.lower() =='cm ':
    convertedweight1=height/100
    print(f'Your height in meters is{convertedweight1}')


else:
    convertedweight2=height*100
    print(f'Your height in centimeters is {convertedweight2}')



print('Enjoy Your Day')