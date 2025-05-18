import re


def map_custom_type(type_str: str) -> str:
    type_str = type_str.strip()

    array_match = re.match(r"(.+?)\[(\d+)\]", type_str)
    if array_match:
        base_type = array_match.group(1).strip()
        size = array_match.group(2)
        return f"{map_custom_type(base_type)}[{size}]"

    direct_map = {
        "int32": "__int32",
        "int16": "__int16",
        "int8": "__int8",
        "uint32": "std::uint32_t",
        "uint16": "std::uint16_t",
        "uint8": "std::uint8_t",
        "uint64": "std::uint64_t",
        "uintptr_t": "std::uintptr_t",
        "float32": "FLOAT",
        "bool": "BOOL",
        "char": "char",
        "Vector": "Vector_t",
        "QAngle": "QAngle_t",
    }
    if type_str in direct_map:
        return direct_map[type_str]

    for old, new in {
        "CHandle": "Handle",
        "CUtlVector": "UtlVector",
        "CRefPtr": "RefPtr",
    }.items():
        match = re.match(rf"{old}\s*<(.+?)>", type_str)
        if match:
            inner = map_custom_type(match.group(1))
            return f"{new}<{inner}>"

    return type_str
