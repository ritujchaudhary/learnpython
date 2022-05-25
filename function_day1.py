##simple function
def greet():
  print("hello")
  print("how are you")
  print("isn't weather nice today")

greet()

## function with input

def greet_with_name(name):
  print(f"hello {name}")
  print(f"how are you {name}")
  print(f"isn't weather nice today {name}")

greet_with_name("Bill")

## function with multiple input  (postional arugements)
def greet_with_(name, location):
    print(f"hello {name} !!")
    print(f"isn't weather nice today in {location}")

greet_with_("bill", "london")

## function with multiple input  (keyword arugements)

def greet_with_(name, location):
    print(f"hello {name} !!")
    print(f"isn't weather nice today in {location}")

greet_with_(location = "london_key", name = "bill_key")


# text = "hello"

# for x in text:
#     print(x)