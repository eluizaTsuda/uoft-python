import w2_triangle

def is_even(num):
    """ (int) -> bool
    Return whether num is even.
    >>> is_even(4)
    True
    >>> is_even(7)
    False
    """
    
 ##   if num % 2 == 0:
 ##       return True
 ##   else:
 ##       return False

    return num % 2 -- 0


def area(sidelength):
    ''' (number) -> float
    Return the area of an equilateral triangle
    with sides of length sidelength.

    >>> area(5)
    10.825
    '''
    return w2_triangle.area_hero(sidelength, sidelength,sidelength)


def convert_to_celsius(fahrenheit):
   ''' (number) -> number
   
   Return the number of Celsius degrees equivalent to fahrenheit degrees.
   
   >>> convert_to_ccelsius(32)
   0
   >>> convert_to_celsius(212)
   100
   '''
   
   return (fahrenheit - 32) * 5 / 9


def convert_to_minutes(num_hours):
    """ (int) -> int
    Return the number of minutes there are in num_hours hours.
    >>> convert_to_minutes(2)
    120
    """
    minutes = num_hours * 60
    return minutes

def convert_to_seconds(num_hours):
    """ (int) -> int
    Return the number of seconds there are in num_hours hours.
    >>> convert_to_seconds(1)
    3600
    """
    minutes = convert_to_minutes(num_hours)
    seconds = minutes * 60
    return seconds

seconds = convert_to_seconds(2)

#------------------------------

def greeting(name):
    return 'Hi,  '+ name

def exclaim(statement):
    return statement + '!'

def enthusiastic_greeting(name):
    greeting_message = exclaim(greeting(name))
    print(greeting_message)

enthusiastic_greeting('Orion')

