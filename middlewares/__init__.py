from loader import dp
from .throttling import ThrottlingMiddleware


def setup():
    if __name__ == "middlewares":
        dp.middleware.setup(ThrottlingMiddleware())
