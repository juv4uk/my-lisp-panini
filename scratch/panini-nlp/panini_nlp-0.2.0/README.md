# Panini-NLP

**A Deterministic, Graph-based, Neuro-symbolic implementation of Pāṇini's Grammar.**

[![](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)


`panini-nlp` is a Python library that decodes the **Aṣṭādhyāyī** not as a static text, but as a computable **Cyclic Directed Graph**. It provides the complete structural context of the grammar—every Sūtra and Dhātu—alongside deterministic engines for Sandhi, Prosody, and Phonetics.

## 📖 About

This project decodes the 2,500-year-old **Aṣṭādhyāyī** as the world's first **Deterministic Generative AI**.

Pāṇini's grammar is not a mere set of rules; it is a **formal generative system** that produces infinite valid Sanskrit words from finite roots using a highly compressed, algebraic source code. `panini-nlp` implements this architecture:
1.  **Universal Registry**: A digital structural map of all 3,996 Sūtras and ~2,000 Dhātus.
2.  **Deterministic Engine**: Mathematical implementation of Sandhi (phonetics) and Chandas (prosody).
3.  **Neuro-Symbolic Bridge**: A GNN layer to handle ambiguity (Vipratisedha) where the deterministic path branches.

We are not inventing AI for Sanskrit; we are decoding the algorithm that was already written.


---

## 🚀 Key Features

### 1. The Complete "Source Code"
Unlike other tools that implement only a few rules, `panini-nlp` contains the **Full Registry**:
- **3,996 Sūtras**: Every rule from the Aṣṭādhyāyī is present as a Python function stub in `panini_nlp/rules/`.
- **~2,000 Dhātus**: Every root from the Dhātupāṭha is registered in `panini_nlp/roots/`.
- **Maheshvara Sutras**: Implements the "Prime Number Architecture" (71.4% prime density) for phoneme compression.

### 2. Hybrid Neuro-Symbolic Architecture
- **Symbolic Core**: Deterministic engines for Sandhi (Euphonic Junction) and Chandas (Prosody).
- **Neural Guidance**: A Graph Neural Network (GNN) layer (`panini_nlp/gnn`) to resolve rule conflicts (Vipratisedha) by learning the graph topology.

### 3. "Seed Kernel" Efficiency
- The core logic fits in **< 50KB**.
- The entire structural knowledge base is generated from raw source texts.

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/meru-os/panini-nlp.git
cd panini-nlp

# Install mostly-pure Python core
pip install .

# Install with Neural Network support (PyTorch)
pip install .[gnn]
```

## 🛠️ Usage Examples

### 1. Deterministic Sandhi (Phonetic Engine v0.2)
Apply formal rules like *Akaḥ Savarṇe Dīrghaḥ* (6.1.101). The engine uses **Varna-Vibhasha** (Phoneme Decomposition) to handle Devanagari input correctly.

```python
from panini_nlp import SandhiEngine

sandhi = SandhiEngine()
result = sandhi.apply("देव", "आलय")
print(result.modified) 
# Output: देवालय (Devalaya) - Rule 6.1.101 applied
```

### 2. Derivation Simulation (Prakriya)
Trace the path of a word through the grammar graph.

```python
# Run the included demo script
# python3 examples/derive_brahman.py

from panini_nlp.rules import registry as rule_registry

# Access Rule 1.1.1 (Growth Definitions)
rule = rule_registry.get("1.1.1")
print(f"{rule.id}: {rule.text}") 
# Output: 1.1.1: vṛddhir ādaic
```

### 3. Prosody Analysis (Chandas)
Analyze the binary rhythm of a verse (Laghu/Guru).

```python
from panini_nlp import ChandasAnalyzer

analyzer = ChandasAnalyzer()
meter = analyzer.analyze("dharmakṣetre kurukṣetre samavetā yuyutsavaḥ")
print(meter.pattern)
# Output: G L G G L G G G ... (Binary Stream)
```

---

## 📂 Project Structure

```text
panini-nlp/
├── panini_nlp/
│   ├── rules/          # 3996 Auto-generated Sutra stubs (Adhyaya 1-8)
│   ├── roots/          # ~2000 Auto-generated Root definitions (Gana 1-10)
│   ├── sandhi.py       # Deterministic Sandhi Engine
│   ├── chandas.py      # Pingala's Binary Prosody Algorithms
│   ├── maheshvara.py   # Prime Number Phonetic Analysis
│   ├── gnn/            # Graph Neural Network Models (PyTorch)
│   ├── data/           # Raw Source Texts (Ashtadhyayi.txt, Dhatupatha.txt)
│   └── validator.py    # Pipeline Orchestrator
├── examples/
│   ├── derive_brahman.py # Paper Example: Derivation of "Brahman"
│   └── derive_shuklam.py # Demo Example: "Shuklam Baradharam" analysis
├── requirements.txt
└── setup.py
```

## License

MIT License. Free for research and education.
