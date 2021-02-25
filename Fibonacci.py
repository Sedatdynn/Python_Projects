def Fibo(n):
   if n <= 1:
       return n
   else:
       return(Fibo(n-1) + Fibo(n-2))

list = []
try:
    nterms = int(input("Please enter a positive term: "))
    if nterms <= 0:
       print("Plese enter a positive integer")
    else:
       print("Fibonacci sequence:")
       for i in range(nterms):
           list.append(Fibo(i))
    print(list)
except:
    print("please enter a integer value.")