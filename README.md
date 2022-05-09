
# `eth_abi_lite`

`eth_abi_lite` is a lite fork of `eth_abi`, aiming to support EVM abi encode/decode functionality without external dependencies on `eth_utils`, `eth_typing`, `toolz`, or `cytoolz`.

`eth_abi_lite` can be used as a drop-in replacement for `eth_abi==3.0.0`.

#### Motivation
1) Many packages in the ethereum ecosystem have conflicting requirements for versions of these dependencies. Pruning these dependencies results in an abi encoding/decoding package that can be included in more environments than `eth_abi`.
2) These dependencies are rather heavy if all you want is basic abi encoding/decoding functionality.

#### Does `eth_abi_lite` work the same as `eth_abi`?

`eth_abi_lite` can be used as a drop-in replacement for `eth_abi==3.0.0`. The one functional difference is that `eth_abi`'s low level pad functions are no longer curry-able. In most cases this difference will not be noticed.

`eth_abi_lite` passes `eth_abi`'s standard test suite when running `tox`:

```
...
======================== 751 passed, 3 skipped in 18.45s ========================
____________________________________ summary ____________________________________
  py37-core: commands succeeded                                                  
  py38-core: commands succeeded                                                  
  py39-core: commands succeeded                                                  
  py310-core: commands succeeded                                                 
  congratulations :)                                                             
```

(tests for linting and docs removed)


#### Is `eth_abi_lite` faster?

According to testing with [tuna](https://github.com/nschloe/tuna) on a good laptop:
- `eth_abi_lite` takes about **18 ms** to import
- `eth_abi` takes about **180 ms** to import

`eth_abi_lite` is faster to import because it loads fewer dependencies. This is useful in the context of cli tools where startup times matter.


## Survey of imported items

`eth_abi_lite` imports the following items from its dependencies:

#### Items Imported From `eth_utils`
- `big_endian_to_int`
- `compose_if_tuple`
- `int_to_big_endian`
- `is_address`
- `is_boolean`
- `is_bytes`
- `is_integer`
- `is_list_like`
- `is_number`
- `is_text`
- `to_canonical_address`
- `to_checksum_address`
- `to_normalized_address`
- `to_tuple`

#### Items Imported From `eth_typing`
- `TypeStr`
- `Decodable`

#### Items Imported From `eth_utils.toolz`
- `toolz.functoolz.curry`


## The Changes
The changes from `eth_abi` to `eth_abi_lite` consist mostly of copying portions of `eth_utils` and `eth_typing`.

The basic idea is that every time something is imported from `eth_utils` or `eth_typing`, that thing is instead imported from a lite version of that package.


#### Step 1. Create `eth_utils_lite`

Copy these items from `eth_utils` to `eth_utils_lite`
- `eth_utils/abi.py`
- `eth_utils/address.py`
- `eth_utils/conversions.py`
- `eth_utils/crypto.py`
- `eth_utils/decorators.py`
- `eth_utils/encoding.py`
- `eth_utils/functional.py`
- `eth_utils/hexadecimal.py`
- `eth_utils/types.py`

The only non-mutual dependency in these modules is `eth_hash.keccak()` in `eth_utils/crypto.py`. Replace this function with `pycryptodome`'s keccak implementation directly.

Also in `eth_utils/functional.py`, remove the functions that are decorated by `toolz.compose`.

It is possible to prune these files more aggressively, but leaving the files unchanged minimizes the chances of introducing bugs.

#### Step 2. Create `eth_typing_lite`

Copy these items from `eth_typing` to `eth_typing_lite`:
- `Address`
- `AnyAddress`
- `ChecksumAddress`
- `Decodable`
- `HexAddress`
- `HexStr`
- `Primitives`
- `TypeStr`

These are all of the `eth_typing` types used by `eth_abi_lite` and `eth_utils_lite`.


#### Step 3. Create `eth_abi_lite`

1. Copy all files from `eth_abi` into `eth_abi_lite`
2. Replace all instances of
    - `eth_utils` with `eth_utils`
    - `eth_typing` with `eth_typing_lite`
    - `eth_abi` with `eth_abi_lite`
3. Replace the `toolz.curry` decoration on `eth_abi.zpad` and `eth_abi.fpad` with `functions.partial` decoration.
