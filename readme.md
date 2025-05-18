# CS2 Schema Dump Parser

A CLI tool to parse/convert CS2 schema dumps into C++ header files.  
Developed based on asphyxia schema dump

---

## Features

- Parses class definitions from schema dump text files.
- Maps custom types to corresponding C++ types.
- Supports generating all classes or a specific class.
- Allows specifying a base class for generated classes.
- Cleans and manages output directory automatically.
- Easily installable via `pip` and usable as a CLI command.

---

## Installation

You can install the package locally for development with:

```bash
git clone https://github.com/LeandroVictor666/cs2-schema-parser.git
cd cs2-schema-parser
pip install .
````

---

## Custom Maps

- You can modify the direct_map dictionary, located in ctypes_map.py, to specify the types you want to use in the dump (e.g., std::int32_t or __int32, fully customizable), **Remember to run 'pip install .' command again**

---

## Usage

````bash
cs2-schema-parser <path_to_dumped_file> [params]
````

---

#### Contact

- GitHub: LeandroVictor666
- Discord: leandrovictor666
- Author: l666.eth0
