import numpy as np


def random_handler(event: dict, context: dict) -> dict:
    lower = event['lower']
    upper = event['upper']
    a = np.random.randint(lower, upper)
    return {'result': a}


if __name__ == '__main__':
    x = random_handler({'upper': 3, 'lower': 1}, {})
    print(x['result'])
