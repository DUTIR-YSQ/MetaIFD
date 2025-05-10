# MetaIFD: Metaphor Understanding and Generation Instruction Fine-tuning Dataset


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

## Example

| **Label**                   | **Value**                                                                                                            |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Sentence**                | The faculty meeting was a real war.                                                                                  |
| **Metaphorical or literal** | Metaphorical                                                                                                         |
| **Metaphor word**           | war                                                                                                                 |
| **Interpretation order**    | 1. The faculty meeting was a peaceful gathering. <br> 2. At the faculty meeting, we talked about real war. <br> 3. The faculty meeting was ridiculous. <br> 4. The faculty meeting was highly aggressive. |
| **Interpretation**          | Using the characteristics of "war" to describe the intensity of the meeting and the challenging nature of the situation. |
| **Metaphor novelty rating** | 0.23                                                                                                                |
| **Metaphor_MIP**            | According to MIP theory, "The faculty meeting was a real war" is a metaphor because the literal meaning of "war" (actual combat) differs from its contextual meaning (an intense and confrontational meeting). |
| **Sentiment**               | -1                                                                                                                  |


## Tasks Supported
| **Task**                    | **Dataset**                                                                 | **Total** |
|-----------------------------|-----------------------------------------------------------------------------|-----------|
| Metaphor Identification      | TroFi, VUA, TSV, MOH, Bizzoni, LCCen, figqa, Katz, GAN-kevin, Reimann      | 113,384   |
| Identify Metaphorical Words  | MOH, MUHCH                                                                  | 5,673     |
| Metaphor Explanation Rating  | Bizzoni, Katz                                                               | 785       |
| Paraphrase Generation        | MUHCH, figqa, Katz                                                          | 8,934     |
| Metaphor Novelty Scoring     | MUNCH                                                                       | 4,070     |
| Sentiment Analysis           | TroFi, VUA, TSV, MOH, Bizzoni, LCCen, figqa, Katz, GAN-kevin, Reimann      | 113,384   |
| **Total**                    |                                                                             | **246,230** |

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
  - Metaphor_MIP.

---


## Data Format

Each dataset entry includes:
- **Sentence:** Full sentence text.
- **Metaphor Indicator:** Whether the sentence contains a metaphor (1 for metaphor, 0 for literal).
- **Metaphor Word(s) number:** The number of metaphorical words included., if applicable.
- **Metaphor Word(s):** The metaphorical word(s) in the sentence, if applicable.
- **Source  Domains:** Conceptual mapping details.
- **Target Domains:** Conceptual mapping details.
- **Interpretations_order:** Metaphor explanations with ratings.
- **Interpretations:** Explain the meaning of metaphor.
- **Novelty Rating:** A score indicating the creativity of the metaphor.
- **Metaphor MIP:** 
The process of identifying metaphors by analyzing and comparing the basic meanings and contextual meanings of metaphorical words in sentences.
- **Sentiment label:** It represents the sentiment orientation of a given sentence, providing information about its emotional polarity. This label is central to sentiment analysis tasks, enabling models to understand and classify the emotional tone of text data. Sentiment orientation is categorized into five levels for finer granularity:
2: Very positive
1: Positive
0: Neutral
-1: Negative
-2: Very negative

---

## Usage

Researchers and developers can use MetaIFD to:
- Fine-tune large language models for metaphor comprehension.
- Benchmark metaphor understanding, explanation, and sentiment analysis capabilities.
- Explore novel training methods for complex language tasks.



## Acknowledgments

MetaIFD was created with contributions from multiple datasets and fine-tuning strategies, aiming to address the limitations of existing metaphor resources. For further details, refer to the accompanying research paper.
