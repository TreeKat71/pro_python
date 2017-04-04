import logging
import math
from time import time

from joblib import Parallel, delayed

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    ts = time()
    res = Parallel(n_jobs=5)(delayed(is_prime)(n) for n in PRIMES)
    print(res)
    print('Took {}s'.format(time() - ts))

if __name__ == '__main__':
    main()


