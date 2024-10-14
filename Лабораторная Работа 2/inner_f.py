def outer_function():
  name = input("Type your name: ")
  age = input("Type your age: ")

  def inner_function():
    print("Inner function output:")
    print("You are " + name + "\nAnd you are " + age + " years old!")
    return {"name": name, "age": age}

  return inner_function()


def call():
  print("return value of inner function: " + str(outer_function()))
