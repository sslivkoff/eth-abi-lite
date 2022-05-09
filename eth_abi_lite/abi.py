from eth_abi_lite.codec import (
    ABICodec,
)
from eth_abi_lite.registry import (
    registry,
)

default_codec = ABICodec(registry)

encode_abi = default_codec.encode_abi
encode_single = default_codec.encode_single
decode_abi = default_codec.decode_abi
decode_single = default_codec.decode_single
is_encodable = default_codec.is_encodable
is_encodable_type = default_codec.is_encodable_type
