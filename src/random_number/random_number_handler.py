from src.random_number.get_random import get_random


def main(event: dict, context: dict) -> dict:
    lower = event['lower']
    upper = event['upper']
    a = get_random(lower, upper)
    return {'result': a}


if __name__ == '__main__':
    x = main({'upper': 3, 'lower': 1}, {})
    print(x['result'])
