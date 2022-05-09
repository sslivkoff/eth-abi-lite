import pytest

from eth_abi_lite.abi import (
    encode_single,
)

from ..common.unit import (
    CORRECT_SINGLE_ENCODINGS,
)


@pytest.mark.parametrize(
    'typ,python_value,abi_encoding,_',
    CORRECT_SINGLE_ENCODINGS,
)
def test_encode_single(typ, python_value, abi_encoding, _):
    actual = encode_single(typ, python_value)
    assert actual == abi_encoding
