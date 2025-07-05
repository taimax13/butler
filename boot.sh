#!/bin/bash
echo "🧠 Booting Strategist Studio..."
python3 strategist/memory_loader.py
python3 runner/run_agent.py
