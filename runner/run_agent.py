import subprocess
from strategist.memory_loader import load_memory

def run_cli():
    memory = load_memory()
    print("\n🚀 Starting agent CLI...")
    print("Type 'exit' to quit.")
    print("---------------------------")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye.")
            break
        print(f"Omni (simulated): I hear you said '{user_input}'. I am reasoning offline.")

if __name__ == "__main__":
    run_cli()
