#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LARATWINS
#
# Created:     23/02/2018
# Copyright:   (c) LARATWINS 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
x = int(input("Please enter an integer: "))
if x < 0:
    x=0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


