def add(a,b):
   return a+b
def sub(a,b):
   return a-b
def multiply(a,b):
   return a*b
def division(a,b):
   if b==0:
     return "ERROR!Division by Zero is not possible."
   return a/b
while True:
  print('-------Advanced Calculator---------')
  print('1.Addition')
  print('2.Subtraction')
  print('3.Multiplication')
  print('4.Division')
  print('5.Exit')
  choice=int(input('Choose an operation between [1-5]: '))
  if choice==5:
    print("Calculator closed succesfully.")
    break
  if choice in ['1','2','3','4']:
    number1=int(input('Enter the first number: '))
    number2=int(input('Enter the second number: '))
     if choice=='1':
       print('Answer: ',add(number1,number2)) 
     elif choice=='2':
       print("Answer: ",sub(number1,number2))
     elif choice=='3':
       print('Answer: ',multiply(number1,number2))
     elif choice=='4':
       print('Answer: ',division(number1,number2))
     else:
        print('Invalid number!, Try again')
