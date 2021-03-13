#Cuando stackeamos decoradores podemos tener resultados inesperados, por como se devuelven los nombres de las
#funciones decoradas
#por eso se puede usar wraps del modulo functools
#
#

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args,**kwargs):

        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2) )
        return result
    return wrapper


import time



@my_logger
@my_timer
def display_info(name, age):
    time.sleep(2)
    print('display info ran with args ({} , {})'.format(name,age))

#display_info = my_logger(my_timer(display_info))
#Eso es lo que pasa si solo se stackean losdecoradores sin mas,
#a la funcion my_logger le llega el nombre de funcion wrapper, en lugar de display_info

display_info('Walter', 26)