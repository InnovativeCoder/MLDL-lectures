n = int(input())

def checkPrime(num) :
  if(num==2) :
    return True

  for i in range(2,num) :
    if(num%i==0):
      return False

  return True

for i in range(2,n+1) :
  if(checkPrime(i)) :
    print(i)
