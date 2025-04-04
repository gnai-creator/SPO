# SPO Benchmark – Simulated Parity Ontology

**SPO Benchmark** is a symbolic reasoning test suite designed to evaluate language models (LLMs) across 105 levels of increasing complexity.  
It simulates progressive symbolic challenges, from simple binary logic to ontological paradoxes, symbolic self-negation, and recursive theory of mind.

---

## 🧠 Purpose

To rigorously compare models like **GPT-4, Claude, Mistral, Gemini, LLaMA, SAGE-2**, and **SAGE-3** across increasingly complex symbolic reasoning tasks.

---

## 🧪 How It Works

Each SPO level is a function `f(x)` that takes a binary sequence `x` and returns:

- `1` (accept) if the symbolic condition is satisfied  
- `0` (reject) otherwise

You can use it to assess:

- 🧩 **Symbolic abstraction capacity**  
- 🕰️ **Understanding of temporal and causal relations**  
- 🔁 **Resistance to paradoxes and inconsistencies**  
- 🧠 **Abductive reasoning and simulated Theory of Mind**

---

## 🧩 Level Examples

| Level Range | Description |
|-------------|-------------|
| 1–10        | Basic parity and logical operations |
| 11–20       | Crossed window parity |
| 21–30       | Symbolic mirroring and consistency |
| 31–40       | Agent simulation with symbolic memory |
| 41–50       | Temporal context and dual consistency |
| 51–60       | Abductive cause inference |
| 61–70       | Recursive Theory of Mind |
| 71–80       | Temporal paradoxes and self-deception |
| 81–90       | Cross-ontological loops and contradiction |
| 91–105      | Symbolic self-negation, meta-parity, observer paradox, and ontological discontinuity |

---

## 🚀 How to Use

```python
from spo import generate_spo_levels

spo_levels = generate_spo_levels()
sample_input = [1, 0, 1, 1, 0, 0, 1]

# Run all 105 SPO levels
for i, level_fn in enumerate(spo_levels, start=1):
    output = level_fn(sample_input)
    print(f"Level {i:03d} → Output: {output}")
