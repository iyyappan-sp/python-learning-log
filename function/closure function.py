



def outer(msg):
    def inner():
        return f"Message is: {msg}"
    return inner

say_hi = outer("Vanakkam Da Mapla")
print(say_hi())
