def greet(name = 'there', message = "Good Morning"):
    """Display a greeting to users"""
    return f"{message} {name}!"

g = greet(message = 'Hello')
print(g)