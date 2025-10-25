"""Remove cryptographic vurze decorators from all functions and classes in a Python file."""

import ast
from typing import List

def remove_decorators(file_path: str) -> str:
    """
    Parse a Python file, remove all @vurze.* decorators from functions and classes, and return the modified code.

    Args:
        file_path: Path to the Python file to process
    Returns:
        Modified Python source code as a string
    """
    with open(file_path, 'r') as f:
        content = f.read()

    tree = ast.parse(content)
    lines = content.split('\n')
    lines_to_remove = set()

    for node in ast.walk(tree):
        if type(node).__name__ in ("FunctionDef", "AsyncFunctionDef", "ClassDef"):
            if hasattr(node, 'decorator_list'):
                for decorator in node.decorator_list:
                    is_vurze_decorator = False
                    if isinstance(decorator, ast.Name):
                        if decorator.id.startswith("vurze"):
                            is_vurze_decorator = True
                    elif isinstance(decorator, ast.Attribute):
                        if isinstance(decorator.value, ast.Name) and decorator.value.id == "vurze":
                            is_vurze_decorator = True
                    elif isinstance(decorator, ast.Call):
                        func = decorator.func
                        if isinstance(func, ast.Attribute):
                            if isinstance(func.value, ast.Name) and func.value.id == "vurze":
                                is_vurze_decorator = True
                        elif isinstance(func, ast.Name) and func.id.startswith("vurze"):
                            is_vurze_decorator = True
                    if is_vurze_decorator:
                        lines_to_remove.add(decorator.lineno - 1)

    found = len(lines_to_remove) > 0
    for line_idx in sorted(lines_to_remove, reverse=True):
        del lines[line_idx]

    modified_code = '\n'.join(lines)
    return modified_code, found
