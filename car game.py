'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''

current_status = input("(START) or (STOP) or (QUIT): ")
if current_status.upper() == "START":
    print("CAR STARTED,READY TO GO" )
elif current_status.upper() =="STOP":
    print("STOP THE CAR")
elif current_status.upper() =="QUIT":
    print("QUIT")
else:
    print("couldn't understand")