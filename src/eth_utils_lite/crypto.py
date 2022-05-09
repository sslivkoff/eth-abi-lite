from typing import Union


from .conversions import to_bytes


def keccak(
    primitive: Union[bytes, int, bool] = None, hexstr: str = None, text: str = None
) -> bytes:
    from Crypto.Hash import keccak as f_keccak

    as_bytes = to_bytes(primitive, hexstr, text)
    return f_keccak.new(digest_bits=256, data=as_bytes).digest()
