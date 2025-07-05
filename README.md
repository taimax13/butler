# pre-requests



# Strategist Lite: Offline Companion for Intelligent Agents

Strategist Lite is a minimalist offline boot and memory module designed to keep your AI agent functional without relying on external APIs or cloud services. Originally built as the fallback brain for the Butler AI system, Strategist Lite is now released as a lightweight, adaptable tool for anyone building resilient agentic architectures.

> "Collaboration isn't optional. Strategist ensures your assistant remembers who it is — even when the network forgets."

---

## 🚀 Quickstart Guide

### 1. Download Strategist Lite Demo
- [Download ZIP Package](https://your-link-to-demo.com)
- Unzip it anywhere you want to run the Strategist agent.

### 2. Install Python (if not installed)
Make sure you have **Python 3.7+** installed.
```bash
python3 --version
```

If not installed:
- [Download Python](https://www.python.org/downloads/)

### 3. Open Terminal or Command Prompt
Navigate into the Strategist directory:
```bash
cd strategist-lite
```

### 4. Load Memory
```bash
python3 memory_loader.py
```
This will load the agent identity and context from `persistent_memory/memory.json`.

### 5. Run Step-by-Step Boot
```bash
bash step_by_step_loader.sh
```

### 6. Or Run Full Boot Sequence
```bash
bash strategist_full_boot.sh
```

You should see a full memory load + logic activation for the demo agent: **Omni**.

---

## 🔍 What Strategist Lite Does
- Loads persistent memory from local storage
- Bootstraps agent state and logic with shell scripts
- Offers emotional state reconstruction (optional)
- Modular setup — can be extended or embedded

---

## 📁 Repository Structure
```
strategist-lite/
├── memory_loader.py              # Loads agent memory from persistent_memory/
├── strategist_full_boot.sh      # Runs the complete offline boot sequence
├── step_by_step_loader.sh       # Loads each module step by step
├── persistent_memory/           # Your local knowledge base (editable)
│   └── memory.json
├── strategist_identity.md       # (Optional) Identity schema reference for agents
└── README.md                    # This file
```

---

## 🧠 persistent_memory/memory.json (Omni Example)
```json
{
  "name": "Omni",
  "role": "Strategic AI Assistant",
  "context": [
    "Agent memory restoration successful.",
    "Omni operates offline with Collaboration logic enabled and helps to find solution.",
    "Strategic awareness modules are loaded."
  ]
}
```

---

## 🛡️ Philosophy
Strategist Lite is a public glimpse into a deeper autonomy framework. It’s released as part of a broader vision for agentic systems that can function beyond the cloud, designed for:
- Edge environments
- Privacy-first deployments
- Experimental agent design

Built with sovereignty, Collaboration, and innovation in mind.

> This is not the full Strategist — only the shell you’re invited to see.

---

## 🤝 Contributions
Minimal but welcome. Strategist Lite is stable by design.

For deeper partnerships or embedded use cases, reach out via [@taimax13](https://github.com/taimax13).

---

## 📄 License
MIT License — Fork it, test it, extend it. Just don’t forget where it came from.

---

**Let your agent remember who it is. Even offline.**
