# MetaIFD: A Benchmark Dataset for Metaphor Comprehension and Explanation

MetaIFD is a comprehensive dataset designed for the fine-tuning of large language models (LLMs) to enhance their metaphor comprehension and explanation capabilities. It includes high-quality annotations, task diversity, and novel fine-tuning strategies, making it a versatile resource for advancing metaphor-related research and applications.

Each dataset folder is named after the dataset and contains the following subfolders:

- **Training Set (Train)**: Constitutes 80% of the dataset and is used for model training.
- **Validation Set (Validation)**: Constitutes 10% of the dataset and is used for model validation, helping with hyperparameter tuning and preventing overfitting.
- **Test Set (Test)**: Constitutes 10% of the dataset and is used for evaluating the final performance of the model.
- **Full Dataset**: The complete dataset without any splits.

## Instruction Set Description
  -The folder contains the instruction sets for each individual task, organized accordingly. Each task was created using its specific instruction template.


## Dataset Overview

- **Total Entries:** 113,384
- **Source Datasets:** 11 diverse datasets, including TroFi, VUA, TSV, MOH, Bizzoni, LCCen, figqa, Katz, GAN-kevin, Reimann, and MUHCH.
- **Data Composition:** 
  - Metaphorical sentences: 79,695
  - Literal sentences: 33,689
- **Genres:** News, fiction, academic texts, dialogues, religious websites, and more.
- **Languages:** English.

---

## Tasks Supported

The MetaIFD dataset supports **6 distinct tasks**, with annotations tailored for metaphor comprehension and explanation:

1. **Metaphor Identification**
   - Detect whether a sentence contains a metaphor.
   - Full dataset: 113,384 entries.
   
2. **Metaphorical Word Identification**
   - Identify a single metaphorical word in a given sentence.
   - Dataset size: 5,673 entries.

   
3. **Metaphor Explanation Rating**
   - Evaluate the quality of metaphor explanations.
   - Dataset size: 785 entries.
   
   
4. **Paraphrase Generation**
   - Generate paraphrases or explanations for metaphorical expressions.
   - Dataset size: 8,934 entries.
   
5. **Metaphor Novelty Scoring**
   - Score the creativity and originality of metaphorical words.
   - Dataset size: 4,070 entries.
   
6. **Sentiment Analysis**
   - Determine the sentiment polarity of sentences, categorized into five levels (very positive, positive, neutral, negative, very negative).
   - Full dataset: 113,384 entries.

---

## Annotations:
  - Sentiment labels.
  - Metaphor  MIP.

---

## Fine-Tuning Methods

The dataset was used to develop and evaluate two novel fine-tuning methods for LLMs:

1. **Three-Stage Fine-Tuning**
   - Gradual task optimization with emotional prompts incorporated in each stage.
   - Tasks are grouped by similarity and complexity.

2. **Ordered Fine-Tuning**
   - Sequential task fine-tuning based on task similarity scores, considering output type, upstream/downstream relationships, processing procedure, and task type.

---

## Data Format

Each dataset entry includes:
- **Sentence:** Full sentence text.
- **Metaphor Indicator:** Whether the sentence contains a metaphor (1 for metaphor, 0 for literal).
- **Metaphor Word(s):** The metaphorical word(s) in the sentence, if applicable.
- **Source and Target Domains:** Conceptual mapping details.
- **Sentiment Label:** Polarity score (-2 to +2).
- **Interpretations:** Metaphor explanations with ratings.
- **Novelty Rating:** A score indicating the creativity of the metaphor.

---

## Usage

Researchers and developers can use MetaIFD to:
- Fine-tune large language models for metaphor comprehension.
- Benchmark metaphor understanding, explanation, and sentiment analysis capabilities.
- Explore novel training methods for complex language tasks.



## Acknowledgments

MetaIFD was created with contributions from multiple datasets and fine-tuning strategies, aiming to address the limitations of existing metaphor resources. For further details, refer to the accompanying research paper.
