'''
Context Manager Using @contextmanager Decorator
https://www.geeksforgeeks.org/context-manager-using-contextmanager-decorator/
'''


# Python program creating a
# context manager

# class ContextManager:
#     def __init__(self):
#         print('init method called')
#
#     def __enter__(self):
#         print('enter method called')
#         return self
#
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print('exit method called')


# Python program for creating a
# context manager using @contextmanager
# decorator

from contextlib import contextmanager

@contextmanager
def DecoratorContextManager(person):
    # Before yield as the enter method
    print(f"Hello {person}")
    yield

    # After yield as the exit method
    print(f"Bye {person}")

def mycontextmanager(func):
    class MyContextManager:
        def __init__(self, *args, **kwargs):
            self.gen = func(*args, **kwargs)

        def __enter__(self):
            next(self.gen)

        def __exit__(self, exc_type, exc_value, exc_traceback):
            try:
                next(self.gen)
            except StopIteration:
                pass

    return MyContextManager

@mycontextmanager
def MyDecoratorContextManager(person):
    # Before yield as the enter method
    print(f"Hello {person}")
    yield

    # After yield as the exit method
    print(f"Bye {person}")

if __name__ == '__main__':

    # Driver code

    print('-'*50 + '[ contextlib decorator context manager ]')

    with DecoratorContextManager('Bob') as manager:
        print('with statement block in context manager')

    print('-'*50 + '[ my decorator context manager ]')

    with MyDecoratorContextManager('Bob') as manager:
        print('with statement block in context manager')