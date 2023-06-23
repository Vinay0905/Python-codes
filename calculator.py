from art import logo

print(logo)

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operators ={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  num1 = int(input("Whts the first number?: "))
  for symbol in operators:
    print(symbol)
  should_cotinue = True
  
  while should_cotinue:
    operation_symbol=input("Pick an operation: ")
    num2=int(input("Whts ur next number?: "))
    calculation_function=operators[operation_symbol]
    answer = calculation_function(num1,num2)


    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f" Type 'y' to continue with {answer} , or type 'n' to start a new calculation : " ) == "y":
      num1 = answer
    else:
      should_cotinue=False
      calculator()

calculator()






