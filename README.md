# Offline Agent Studio (Demo Build)

This is a fully offline demo of an AI assistant called **Omni**, powered by Strategist memory and designed to operate without internet or cloud dependency.

## 🚀 How to Run

1. Unzip the project.
2. Make the boot script executable:
   ```bash
   chmod +x boot.sh
   ```

3. Run the full system:
   ```bash
   ./boot.sh
   ```

This loads memory, boots strategist identity, and launches an offline CLI loop.

## 📦 What’s Included

- `strategist/` contains memory and identity
- `runner/` contains local loop and model prompt placeholders
- `models/` is ready to accept `.gguf` LLMs

## 📥 Model Loading (Coming in v2)

You’ll be able to plug in Mistral, LLaMA, or Phi models with llama.cpp runner script.

## 🧠 Omni's Philosophy

Omni runs with sovereignty-first design — capable of booting without cloud, API keys, or internet.

