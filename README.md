# 🛰️ Unstoppable v2 – Open Source AI Swarm Framework

A local-first, agent-coordinated, modular AI orchestration system designed for real-world transparency, resilience, and zero dependency on cloud services.

## 🧠 What This Is

**Unstoppable v2** implements:
- Multi-agent coordination with LoRA personas and scoped memory
- Full local inference using open LLMs via `llama.cpp`
- Retrieval-augmented rehydration using vector memory (Spectra RAG)
- Optional trustless append-only audit trail (Spectra’s ITL ledger)
- Streamlit-based UI for demo and debugging
- Hierarchical swarm orchestration, parallel execution, and persona overlays

## 📂 Directory Structure

```
unstoppable-swarm/
├── cli.py
├── README.md
├── LICENSE
├── .gitignore
├── src/
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── coder_agent.py
│   │   └── verifier_agent.py
│   ├── orchestrator/
│   │   ├── orchestrator.py
│   │   └── agent_interface.py
│   ├── memory/
│   │   ├── vector_store.py
│   │   ├── rehydrate.py
│   │   └── ingest.py
│   ├── ledger/
│   │   ├── ledger.py
│   │   └── reputation.py
│   ├── semantic/
│   │   └── field_zero.py
│   ├── utils/
│   │   └── logger.py
│   └── personas/
│       └── [LoRA adapters, metadata, etc.]
├── data/
│   ├── docs/
│   └── tokens/
├── models/
│   └── [gguf model files]
├── ui/
│   └── app.py
├── requirements.txt
├── Dockerfile
```

## 🚀 Quick Start

Run a sample CLI swarm task:

```bash
python cli.py
```

You should see:

```
Unstoppable v2 CLI scaffold: Swarm orchestrator loading soon.
```

## 📦 Goals

- ✅ Swarm CLI scaffold
- ✅ Local vector memory
- ✅ Signed trust log prototype
- 🛠️ Agents with role + persona overlays
- 🛠️ Streamlit swarm panel
- 🛠️ Multisig & CRDT sync in ITL ledger

## 🧠 Philosophy

No prompt-stuffing. No black-box cloud. No silent drift.  
You can inspect every retrieval, every token, every log entry.

Sovereign, semantic, swarm-native.

---

MIT License
