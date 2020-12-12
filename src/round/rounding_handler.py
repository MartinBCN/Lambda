from src.random_number.get_random import get_random
import numpy as np


def main(event: dict, context: dict) -> dict:
    x = event['number']
    a = np.round(x)
    return {'result': a}


if __name__ == '__main__':
    x = main({'number': 3.1}, {})
    print(x['result'])
