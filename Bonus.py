# Bonus. Write a function that when given two numbers, finds their greatest common divisor.

def gcd(x,y):
  if y == 0:
    return x
  else:
    return gcd(y, x % y)

print("gcd of 15 and 10:",gcd(15,10))
print("gcd of 46 and 12:",gcd(46,12))

def gcd(a,b): 
    print(f"a{a} -- b{b}") 
    if b==0: 
        print(f"a{a} -- b{b}") 
        return a 
    else: 
        print(f"a{a} -- b{b}-- a%b{a%b}") 
        return gcd(b,a%b)
gcd(15,20)