#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LARATWINS
#
# Created:     22/02/2018
# Copyright:   (c) LARATWINS 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
stringVar = "abcdefghijkxxxxxxxabcedf"
loc = stringVar.count('x')
print loc
lo = stringVar.find('j')
print lo
string = stringVar.lower()
print string
Var = stringVar.upper()
print Var
Va = stringVar.replace('x', 'y',2)
print Va
stringVar = stringVar.strip('f')
print stringVar


