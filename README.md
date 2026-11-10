# MetaIFD: A Benchmark Dataset and Instruction Fine-tuning Methods for Metaphorical Comprehension and Explanation

**MetaIFD** (Metaphor Understanding and Generation Instruction Fine-Tuning Dataset) is a benchmark for instruction fine-tuning of large language models on metaphor comprehension and explanation. It aggregates and re-annotates **113,384 sentences** from 11 public metaphor datasets, provides **246,230 task instances** across six tasks, and ships ready-to-use instruction sets together with a three-stage fine-tuning recipe.

The dataset accompanies the paper:

> Senqi Yang, Dongyu Zhang, Wei Guo, Mingshuo Pan, Haojia Li, Liang Yang, Hongfei Lin. **A Benchmark Dataset and Instruction Fine-Tuning Methods for Metaphorical Comprehension and Explanation.** *Database Systems for Advanced Applications (DASFAA 2025)*, Lecture Notes in Computer Science, vol. 15989, pp. 499–508. Springer. DOI: [10.1007/978-981-95-4149-2_33](https://doi.org/10.1007/978-981-95-4149-2_33)

## Dataset overview

| Item | Value |
|---|---|
| Sentences | 113,384 |
| Metaphorical sentences | 79,695 |
| Literal sentences | 33,689 |
| Task instances | 246,230 |
| Tasks | 6 |
| Source datasets | 11 |
| Language | English |
| Genres | News, fiction, academic texts, dialogues, religious websites, and others |

Each source dataset folder contains a full annotation file plus fixed **80% / 10% / 10%** train / validation / test splits (`*_train.json`, `*_val.json`, `*_test.json`).

## Repository structure

```
MetaIFD/
├── dataset/
│   ├── Trofi/                 # TroFi
│   ├── VUA/                   # VUA
│   ├── TSV/                   # TSV
│   ├── MOH/                   # MOH
│   ├── bizzoni/               # Bizzoni
│   ├── LCCen/                 # LCCen
│   ├── figqa/                 # figqa
│   ├── Katz/                  # Katz
│   ├── Katzinverse/           # Katz, inverse label setting
│   ├── kevin/                 # GAN-kevin
│   ├── Reimann/               # Reimann
│   ├── MUHCHgeneration/       # MUHCH, generation subset
│   └── MUHCHjudgement/        # MUHCH, judgement subset
├── instruct_set/
│   ├── instruct_Binary_classification.json
│   ├── instruct_identift_word.json
│   ├── instruct_explanation_rating.json
│   └── instruct_metaphor_novelty.json
├── LICENSE
└── README.md
```

Each dataset directory contains:

- `<name>.json` — the complete annotated dataset;
- `<name>_train.json`, `<name>_val.json`, `<name>_test.json` — 80% / 10% / 10% splits.

## Source datasets

MetaIFD is built on the following public resources:

| Folder | Source dataset |
|---|---|
| `Trofi` | TroFi |
| `VUA` | VUA metaphor corpus |
| `TSV` | TSV |
| `MOH` | MOH |
| `bizzoni` | Bizzoni |
| `LCCen` | LCCen |
| `figqa` | figqa |
| `Katz` | Katz |
| `Katzinverse` | Katzinverse |
| `kevin` | GAN-kevin |
| `Reimann` | Reimann |
| `MUHCHgeneration`, `MUHCHjudgement` | MUHCH |

## Tasks

MetaIFD supports six tasks with task-specific annotations:

| Task | Source datasets | Instances |
|---|---|---|
| Metaphor Identification | TroFi, VUA, TSV, MOH, Bizzoni, LCCen, figqa, Katz, GAN-kevin, Reimann | 113,384 |
| Metaphorical Word Identification | MOH, MUHCH | 5,673 |
| Metaphor Explanation Rating | Bizzoni, Katz | 785 |
| Paraphrase Generation | MUHCH, figqa, Katz | 8,934 |
| Metaphor Novelty Scoring | MUHCH | 4,070 |
| Sentiment Analysis | TroFi, VUA, TSV, MOH, Bizzoni, LCCen, figqa, Katz, GAN-kevin, Reimann | 113,384 |
| **Total** | | **246,230** |

1. **Metaphor Identification** — decide whether a sentence contains a metaphor.
2. **Metaphorical Word Identification** — locate the metaphorical word(s) in a sentence.
3. **Metaphor Explanation Rating** — rate the quality of a candidate metaphor explanation.
4. **Paraphrase Generation** — generate an explanation or paraphrase for a metaphorical expression.
5. **Metaphor Novelty Scoring** — score the creativity and originality of a metaphor.
6. **Sentiment Analysis** — assign one of five sentiment levels (very positive, positive, neutral, negative, very negative).

## Instruction sets

`instruct_set/` contains instruction-tuning data for the tasks, each instance in the standard format:

```json
{
  "instruction": "...",
  "input": "",
  "output": "..."
}
```

For example:

```json
{
  "instruction": "[ the flowers danced in the wind ]. A metaphor refers to an implied comparison that links two fundamentally different things or concepts to convey a certain meaning or feeling. Is this sentence a metaphor?",
  "input": "",
  "output": "Yes. The sentence \"the flowers danced in the wind\" contains a metaphor where dancing is attributed to the flowers, implying a graceful, rhythmic movement akin to human dance."
}
```

## Instruction fine-tuning

The paper proposes a **three-stage instruction fine-tuning strategy** guided by two ordering principles:

1. **Explicit sentiment tasks before implicit sentiment tasks** — train on tasks with explicit sentiment supervision first, then move to tasks where sentiment must be inferred from the metaphor.
2. **Understanding tasks before generation tasks** — first train metaphor comprehension tasks, then generation tasks such as paraphrase generation.
3. **Difficulty-based training across tasks** — tasks are ordered by difficulty so that later stages build on earlier capabilities.

The paper reports improvements on all six tasks after instruction fine-tuning with this schedule.

## Data format

A dataset record looks like this:

```json
{
  "ID": 0,
  "Sentence": "A bagpipe is a newborn baby.",
  "Metaphor": 1,
  "Metaphor_word_number": null,
  "Metaphor_word": null,
  "Source_domain": null,
  "Target_domain": null,
  "Metaphor_span_types": null,
  "Metaphor_interpretation_order": [
    "A bagpipe is loud.#4",
    "A bagpipe is delicate.#3",
    "A bagpipe is a musical instrument.#2",
    "A bagpipe is quiet.#1"
  ],
  "Alternative_words": null,
  "interpretation": null,
  "Language": "English",
  "Metaphor_novelty_rating": null,
  "Metaphor_why": "The metaphor \"A bagpipe is a newborn baby\" involves mapping attributes of a newborn baby onto a bagpipe, implying qualities such as novelty, potential, and fragility.",
  "sentimental_label": 0
}
```

| Field | Description |
|---|---|
| `ID` | Sample identifier within the source dataset. |
| `Sentence` | The sentence to be analysed. |
| `Metaphor` | `1` if the sentence is metaphorical, `0` if literal. |
| `Metaphor_word_number` | Number of metaphorical words, if annotated. |
| `Metaphor_word` | The metaphorical word(s), if annotated. |
| `Source_domain` | Source domain of the conceptual mapping, if annotated. |
| `Target_domain` | Target domain of the conceptual mapping, if annotated. |
| `Metaphor_span_types` | Span type of the metaphorical expression, if annotated. |
| `Metaphor_interpretation_order` | Candidate interpretations with quality ratings, in the form `interpretation#rating`. |
| `Alternative_words` | Alternative metaphorical words, if annotated. |
| `interpretation` | Natural-language explanation of the metaphor, if annotated. |
| `Language` | Language of the sentence (English in this release). |
| `Metaphor_novelty_rating` | Creativity / novelty score, if annotated. |
| `Metaphor_why` | Analysis of why the expression is metaphorical, following the MIP procedure. |
| `sentimental_label` | Sentiment polarity: `2` very positive, `1` positive, `0` neutral, `-1` negative, `-2` very negative. |

Fields that were not annotated for a particular source dataset are `null`.

## Loading example

```python
import json
from pathlib import Path

root = Path("MetaIFD")

# One source dataset, with its predefined splits
with open(root / "dataset" / "Trofi" / "Trofi_train.json", encoding="utf-8") as f:
    train = json.load(f)

print(len(train))
print(train[0]["Sentence"])
print(train[0]["Metaphor_word"], train[0]["sentimental_label"])

# Instruction-tuning set
with open(root / "instruct_set" / "instruct_Binary_classification.json", encoding="utf-8") as f:
    instructions = json.load(f)

print(instructions[0])
```

The splits are ordinary JSON arrays, so they can also be loaded with pandas or the Hugging Face `datasets` library.

## Licensing

- **Annotations, instruction sets, and splits** produced for MetaIFD are released under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**: <https://creativecommons.org/licenses/by-nc/4.0/>.
- **Sentences and source annotations** come from the public datasets listed above and remain subject to the licenses and terms of those original datasets. Please check and comply with each source dataset's license before use.
- MetaIFD is provided **solely for non-commercial academic research**.

If you believe that any content in this dataset infringes your rights, please contact the authors and the material will be removed.

## Citation

If you use MetaIFD, please cite:

```bibtex
@inproceedings{yang2025metaifd,
  title     = {A Benchmark Dataset and Instruction Fine-Tuning Methods for Metaphorical Comprehension and Explanation},
  author    = {Yang, Senqi and Zhang, Dongyu and Guo, Wei and Pan, Mingshuo and Li, Haojia and Yang, Liang and Lin, Hongfei},
  booktitle = {Database Systems for Advanced Applications (DASFAA 2025)},
  series    = {Lecture Notes in Computer Science},
  volume    = {15989},
  pages     = {499--508},
  year      = {2025},
  publisher = {Springer},
  doi       = {10.1007/978-981-95-4149-2_33}
}
```

## Acknowledgments

MetaIFD is built on the TroFi, VUA, TSV, MOH, Bizzoni, LCCen, figqa, Katz, GAN-kevin, Reimann, and MUHCH datasets. We thank the authors of these resources for making them publicly available.
