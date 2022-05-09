import typing


Decodable = typing.Union[bytes, bytearray]
Primitives = typing.Union[bytes, int, bool]
TypeStr = str
HexStr = typing.NewType('HexStr', str)

Address = typing.NewType('Address', bytes)
HexAddress = typing.NewType('HexAddress', HexStr)
ChecksumAddress = typing.NewType('ChecksumAddress', HexAddress)
AnyAddress = typing.TypeVar('AnyAddress', Address, HexAddress, ChecksumAddress)
