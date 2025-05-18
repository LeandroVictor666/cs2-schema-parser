import re
from typing import List, Tuple, Dict

FIELD_REGEX = re.compile(r"(.+?)\s+(\w+)\s*=\s*0x[0-9A-Fa-f]+")


def parse_all_classes(dump_text: str) -> Dict[str, List[Tuple[str, str, str]]]:
    classes = {}
    current_class = None

    for line in dump_text.strip().splitlines():
        line = line.strip()
        if line.startswith("class "):
            current_class = line.split()[1]
            classes[current_class] = []
        elif current_class:
            match = FIELD_REGEX.match(line)
            if match:
                type_name, var_name = match.groups()
                classes[current_class].append((type_name.strip(), var_name, var_name))
    return classes
