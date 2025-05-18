from typing import List, Tuple
from .ctypes_map import map_custom_type


def generate_cpp(
    class_name: str, fields: List[Tuple[str, str, str]], base_class: str = ""
) -> str:
    base_decl = f" : public {base_class}" if base_class else ""
    lines = [f"class {class_name}{base_decl}", "{", "public:"]

    for original_type, method_name, var_name in fields:
        cpp_type = map_custom_type(original_type)
        lines.append(
            f'\tSCHEMA_ADD_FIELD({cpp_type}, {method_name}, "{class_name}->{var_name}");'
        )

    lines.append("};")
    return "\n".join(lines)
