import hashlib
import random
import string
from typing import Iterator

SALT_LENGTH: int = 16
HASH_LENGTH: int = 128
IDENTIFIER_LENGTH: int = SALT_LENGTH + HASH_LENGTH


def salt_function() -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(SALT_LENGTH))


def hash_function(s: str) -> str:
    return hashlib.sha512(s.encode()).hexdigest()


def generate_identifier(unique: str) -> Iterator[str]:
    """Generate a new identifier.

    This will continue to yield new identifiers until a unique one is
    found, as decided by the caller.
    """

    while True:
        salt = salt_function()
        yield salt + hash_function(salt + unique)
