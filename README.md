# 🛰️ Unstoppable v2 – Open Source AI Swarm Framework

A local-first, agent-coordinated, modular AI orchestration system designed for real-world transparency, resilience, and **zero dependency on cloud services**.

---

## ✅ System Status

This repo contains the **working implementation** of Unstoppable v2:

- 🔁 **Planner → Coder → Verifier** agent loop
- 🧠 **Spectra Rehydration Paradigm** (compressed vector memory → rehydrated answers)
- 🧮 **LLM inference powered by llama.cpp** (offline `.gguf` model)
- 🧾 Fully inspectable prompt construction + output verification
- 💻 Zero external API calls. **All execution is local**.
- 🔧 Runs on CPU or GPU using quantized models like `mistral-7b-instruct-v0.2.Q4_K_M.gguf`

---

## 📂 Directory Structure

```
unstoppable-swarm/
├── cli.py                     # Main entry point for swarm execution
├── README.md
├── LICENSE
├── .gitignore
├── models/                    # Place your .gguf model here (e.g. mistral-7b-instruct-v0.2.Q4_K_M.gguf)
├── data/
│   └── docs/                  # Optional custom doctrine fragments
├── src/
│   ├── agents/                # All agent logic
│   │   ├── planner_agent.py
│   │   ├── coder_agent.py     ← Uses rehydration + LLM inference
│   │   ├── verifier_agent.py
│   │   └── llm.py             ← llama.cpp wrapper
│   ├── orchestrator/
│   │   ├── orchestrator.py
│   │   └── agent_interface.py
│   ├── memory/
│   │   ├── ingest.py          ← Loads doctrine into Chroma vector DB
│   │   ├── vector_store.py    ← Chroma wrapper
│   │   └── rehydrate.py       ← Query+prompt builder
```

---

## 🚀 How to Run It

### 1. Install requirements (in a fresh `.venv`)
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install llama-cpp-python chromadb sentence-transformers numpy
```

### 2. Download a `.gguf` model
Recommended:
- [`mistral-7b-instruct-v0.2.Q4_K_M.gguf`](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)

Place it in:
```
models/mistral-7b-instruct-v0.2.Q4_K_M.gguf
```

### 3. Ingest doctrine into memory
```bash
python -m src.memory.ingest
```

### 4. Run the CLI swarm
```bash
python cli.py
```

---

## 🧠 Example Prompt

```text
> Explain Spectra’s collapse-and-rehydration memory design in plain English.
```

✔️ Context will be retrieved from vector memory  
✔️ Coder agent rehydrates it into a full answer  
✔️ Verifier signs off on the result  

---

## 🛤️ Roadmap

The following components are modular and will be layered in next:

- 🧾 ITL Ledger (trustless append-only log)
- 🧠 Field Zero drift/fork/tension tracker
- 🖥️ Streamlit UI (multi-agent dashboard)
- 🧩 Persona overlays (LoRA adapters per agent)

---

## 🧭 Philosophy

No prompt-stuffing.  
No cloud hallucinations.  
No startup required.

This is **sovereign AI** — embedded memory, post-cloud execution, and transparent reasoning.

---

MIT License
