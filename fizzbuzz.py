def fizzBuzz(nombre):
    if nombre % 15 == 0:
        return 'fizzBuzz'
    elif nombre % 3 == 0:
        return 'fizz'
    elif nombre % 5 == 0:
        return 'Buzz'
    else:
        return nombre
