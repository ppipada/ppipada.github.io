from functools import wraps
from closures import chain_closures
import logging

logger = logging.getLogger()

def x(a):
    def request_logger(f):
        @wraps(f)
        def rlog(*args, **kwargs):
            logger.info("%s x entry", a)
            ret = f(*args, **kwargs)
            logger.info("%s x exit", a)
            return ret

        return rlog

    return request_logger


def y(b):
    def request_logger(f):
        @wraps(f)
        def rlog(*args, **kwargs):
            logger.info("%s y entry", b)
            ret = f(*args, **kwargs)
            logger.info("%s y exit", b)
            return ret

        return rlog

    return request_logger


def z(a, b):
    c1 = x(a)
    c2 = y(b)

    def request_logger(f):
        @wraps(f)
        def rlog(*args, **kwargs):
            q = c1(c2(f))
            logger.info("z entry")
            ret = q(*args, **kwargs)
            logger.info("z exit")
            return ret

        return rlog

    return request_logger


def w(a, b, f):
    c1 = x(a)
    c2 = y(b)
    q = c1(c2(f))
    return q


def get_w(a, b):
    c1 = x(a)
    c2 = y(b)
    q = chain_closures([c1, c2])
    return q


def f1(a, b):
    logger.info("%s %s", a, b)
    # raise Exception("me except")


def smain():
    c4 = get_w(10, 11)
    f2 = c4(f1)
    f2(12, 13)
    logger.info(f2.__name__)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    smain()
