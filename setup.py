#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

HYPOTHESIS_REQUIREMENT = "hypothesis>=4.18.2,<5.0.0"

extras_require = {
    'tools': [
        HYPOTHESIS_REQUIREMENT,
    ],
    'test': [
        "pytest>=6.2.5,<7",
        "pytest-pythonpath>=0.7.1",
        "pytest-xdist>=2.5.0,<3",
        "tox>=2.9.1,<3",
        "eth-hash[pycryptodome]",
        "toolz",
        HYPOTHESIS_REQUIREMENT,
    ],
    'lint': [
        "flake8==4.0.1",
        "isort>=4.2.15,<5",
        "mypy==0.910",
        "pydocstyle>=3.0.0,<4",
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
        "towncrier>=19.2.0, <20",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +  # noqa: W504
    extras_require['test'] +  # noqa: W504
    extras_require['lint'] +  # noqa: W504
    extras_require['doc']
)


with open('./README.md') as readme:
    long_description = readme.read()


setup(
    name='eth_abi_lite',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='3.0.2',
    description="""eth_abi_lite is a lite fork of `eth_abi`, aiming to support EVM abi encode/decode functionality without external dependencies on `eth_utils`, `eth_typing`, `toolz`, or `cytoolz`""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sslivkoff/eth-abi-lite',
    include_package_data=True,
    install_requires=[
        'parsimonious>=0.8.0,<0.9.0',
    ],
    python_requires='>=3.7, <4',
    extras_require=extras_require,
    py_modules=['eth_abi_lite'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    package_dir={"": 'src'},
    packages=[
        'eth_abi_lite',
        'eth_abi_lite.tools',
        'eth_abi_lite.utils',
        'eth_utils_lite',
        'eth_typing_lite',
    ],
    package_data={'eth_abi_lite': ['py.typed']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
