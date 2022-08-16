import time
#Python divmod()
# The divmod() method takes two numbers as arguments and 
# eturns their quotient and remainder in a tuple.
# \r moves the cursor to the beginning of the line and then keeps outputting characters as normal. 

def count_down_timer(timer):
    while timer:
        min, sec = divmod(timer, 60)
        time_format = '{:02d} : {:02d} '.format(min, sec)
        print(time_format, end='/r ')
        time.sleep(1)
        timer -= 1


        print("stop")
num = int(input("Set your input in sec: "))
count_down_timer(num)