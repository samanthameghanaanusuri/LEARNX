# -*- coding: utf-8 -*-
"""
Builder script for Python Course Rebuild
"""
import os
import importlib.util

def load_module(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def build():
    print("Building python_course_rebuild.py...")
    modules_data = []
    
    # Load 15 modules
    for i in range(1, 16):
        file_path = os.path.join(os.path.dirname(__file__), f"module{i}.py")
        if os.path.exists(file_path):
            mod = load_module(f"module{i}", file_path)
            modules_data.append(mod.MODULE_DATA)
        else:
            print(f"Warning: {file_path} not found. Skipping Module {i}.")
            
    # Write the output file
    out_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "python_course_rebuild.py")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("\"\"\"\nLEARNX Python Course Rebuild Content\n\"\"\"\n\n")
        f.write("PYTHON_REBUILD_MODULES = [\n")
        
        for idx, mod in enumerate(modules_data):
            f.write(repr(mod))
            if idx < len(modules_data) - 1:
                f.write(",\n")
            else:
                f.write("\n")
                
        f.write("]\n")
        
    print(f"Successfully wrote {len(modules_data)} modules to {out_path}.")

if __name__ == "__main__":
    build()
