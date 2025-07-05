import json
import os

def load_memory(path="persistent_memory/memory.json"):
    if not os.path.exists(path):
        print(f"❌ Memory file not found at {path}")
        return None
    with open(path, "r") as file:
        memory = json.load(file)
        print(f"✅ Loaded memory for: {memory.get('name')}")
        for line in memory.get("context", []):
            print(f" - {line}")
    return memory

if __name__ == "__main__":
    load_memory()
