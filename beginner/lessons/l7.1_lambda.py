"""
Lesson 7.1: Lambda Functions

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python
"""


# Lambda function:
lambda_function = lambda x, y: x + y


# Function equivalent:
def function_equivalent(x, y):
    return x + y


print(lambda_function(5, 3) == function_equivalent(5, 3))
