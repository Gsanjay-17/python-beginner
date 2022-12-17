'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''

weight=input('enter your weight: ')
unit=input('(L)bs or (K)kg: ')
if unit=="L":
    weight_kg=int(weight)*0.45
    print(weight_kg)
elif unit=="K":
    weight_pd=int(weight)*2.205
    print(weight_pd)
else:
    print('invalid unit')
