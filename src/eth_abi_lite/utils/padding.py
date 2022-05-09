import functools


def zpad(value: bytes, length: int) -> bytes:
    return value.rjust(length, b'\x00')


zpad32 = functools.partial(zpad, length=32)


def zpad_right(value: bytes, length: int) -> bytes:
    return value.ljust(length, b'\x00')


zpad32_right = functools.partial(zpad_right, length=32)


def fpad(value: bytes, length: int) -> bytes:
    return value.rjust(length, b'\xff')


fpad32 = functools.partial(fpad, length=32)
