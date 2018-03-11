total = 0
def sum( arg1, arg2 ):
   total = arg1 + arg2
   print("Total inside function:",total)
   return total
   
sum( 10, 20 )
print( "Total outside funtion: ", total) 
