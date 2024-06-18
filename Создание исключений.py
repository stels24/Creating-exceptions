class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message

class ProcessingException(Exception):
    def __init__(self, message):
        self.message = message


def example(a, b):
    if type(a) is str:
        raise InvalidDataException('вместо "а" подставь число')
    if type(b) is str:
        raise ProcessingException('вместо "b" подставь число')
    return (a + 5 * b)

def work(a, b):
    try:
        print(example(a,b))
    except (InvalidDataException, ProcessingException) as err:
        print(f'{err.message}')
        raise

try:
    work(2, '8')
except Exception:
    print('ещё не решено?')
else: print('верное решение')


print()
try:
    work(2, 8)
except Exception:
    print('ещё не решено?')
else: print('верное решение')