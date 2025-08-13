# MinecraftGPT API

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

The **MinecraftGPT API** is the central AI backend for all [MinecraftGPT](https://github.com/MinecraftGPT) projects.

---

## 📚 Documentation

**For full installation, configuration, and API reference, please visit our documentation website.**

---

## 🚀 Quick Start

### 1. Clone the Repo
```bash
git clone https://github.com/MinecraftGPT/minecraft-gpt-api.git
cd api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure
1.  Copy `config.yml.example` to `config.yml`.
2.  Add your `openrouter_api_key` to `config.yml`.

### 4. Run
```bash
uvicorn main:app --reload
```

---