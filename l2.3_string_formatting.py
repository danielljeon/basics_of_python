"""
Lesson 2.3: String Formatting

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""

"""
Formatting strings allows us to put the values into strings and are especially useful for print 
statements.

Generally speaking the best way to format strings in Python 3.6+ is by using f-strings. The 
expressions inside the braces are evaluated in runtime and then combined with the string part of 
the f-string after which the final value is returned.

String formatting with f-strings...
"""

x = "times"
y = 5.0
z = 10e2
val = f"2 {x} ({y} + {z}) is equal to {2 * (y + z)}"  # String literals (f-strings).
print(val)  # Prints "2 times (5.0 + 1000.0) is equal to 2010.0".

num = 3.1415
val = f"The value of pi is: {num:2.{5}f}"  # Here we format the num to 5 decimal points.
print(val)  # Prints "The value of pi is: 3.14150".

"""
String formatting with the % operator...

- "%d" for integers
- "%f" for floating-point numbers
- "%b" for binary numbers
- "%o" for octal numbers
- "%x" for octal hexadecimal numbers
- "%s" for string
- "%e" for floating-point in an exponent format
"""

val = "2 %s (%f + %e) is equal to %f" % (x, y, z, 2 * (y + z))
print(val)  # Prints "2 times (5.000000 + 1.000000e+03) is equal to 2010.000000".
# Notice here how the values are cast based on the % operator and the floating point precision.

val = "The value of pi is: %1.5f" % num  # Here we format the num to 5 decimal points.
print(val)  # Prints "The value of pi is: 3.14150"

"""
String formatting using the format function...

"{}" takes the place we were would like to insert values.

NOTE: This should ideally only be used for versions earlier than Python 3.6, f-strings were 
introduced specifically with simplicity, performance and readability improvements over .format().
"""

val = "2 {} ({} + {}) is equal to {}".format(x, y, z, 2 * (y + z))
print(val)  # Prints "2 times (5.0 + 1000.0) is equal to 2010.0".

val = "The value of pi is: {0:1.5f}".format(num)  # Here we format the num to 5 decimal points.
print(val)  # result = "The value of pi is: 3.14150"
