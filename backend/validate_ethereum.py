import re


def is_valid_ethereum_address(address):
    pattern = re.compile("^0x[a-fA-F0-9]{40}$")
    return bool(pattern.match(f"{address}"))


print(
    "Is valid ethreum address is ",
    is_valid_ethereum_address("public_key_metamask"),
)
