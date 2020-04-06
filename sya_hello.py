def new_dec(func):
    def wrapper(name):
        msg=func(name)
        msg=msg.upper()
        return msg
    return wrapper

@new_dec
def say_hello(name):
      return "Hello " + name




ans=say_hello("Ravi")
print(ans)
