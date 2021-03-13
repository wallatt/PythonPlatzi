def decorator_function(original_function):
    def wrapper_function(*args, **kwargs): #nombres de convencion, pero permiten que la funcion decorada reciba
                                            #cualquier numero de argumentos.
        print('wrapper function ran this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('display info ran with arguments ({}, {})'.format(name, age))


display()
display_info('John', 25)
