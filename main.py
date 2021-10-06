'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if (n==0 or n==1):
    return False
  for d in range(2, n//2):
    if (n%d==0):
      return False
  return True
 
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  prod = 1
  for el in range(0, len(lst)):
      prod = prod * lst[el]
  return prod
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(a, b):
  # codul vostru aici
  while b:
    r = a%b
    a = b
    b = r
  return a
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(m, n):
  # codul vostru aici
  while m != n:
    if m>n:
      m = m - n
    else:
      n = n - m
  return m

def main():
  # interfata de tip consola aici
  print('''
    1. Is prime
    2. Product
    3. Cmmdc ver1
    4. Cmmdc ver2
''')
  x = int(input("Comanda:"))
  if (x == 1):
      # is prime
      n = int(input("Introduceti n="))
      print(is_prime(n))
  if (x == 2):
      # product
      n = int(input("Introduceti n="))
      list = []
      for i in range(0, n):
          el = int(input())
          list.append(el)
      print(list)
      print(len(list)) # lungimea listei
      print("Produsul este =", get_product(list))
  if (x == 3):
      # cmmdc ver1
      a = int(input("Introduceti a="))
      b = int(input("Introduceti b="))
      print("Cmmdc este: ", get_cmmdc_v1(a,b))
  if (x == 4):
      # cmmdc ver2
      m = int(input("Introduceti m="))
      n = int(input("Introduceti n="))
      print("Cmmdc este: ", get_cmmdc_v2(m,n))
      
if __name__ == '__main__':
  main()
