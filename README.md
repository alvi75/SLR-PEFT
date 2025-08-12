# A Systematic Literature Review of Parameter-Efficient Fine-Tuning for Large Code Models

## Abstract

The rise of Artificial Intelligence (AI)—and particularly Large Language Models (LLMs) for code—has reshaped Software Engineering (SE) by enabling the automation of tasks such as code generation, bug detection, and repair. However, these models require significant computational resources for training and fine-tuning, posing challenges for real-world adoption in resource-constrained environments. To address this, the research community has increasingly turned to Parameter-Efficient Fine-Tuning (PEFT)—a class of techniques that enables the adaptation of large models by updating only a small subset of parameters, rather than the entire model. In this Systematic Literature Review (SLR), we examine the growing application of PEFT techniques across a wide range of software engineering tasks. We analyze how these methods are used to optimize various deep learning (DL) architectures, focusing on their impact on both performance and efficiency. Our study synthesizes findings from 28 peer-reviewed papers, identifying patterns in configuration strategies and adaptation trade-offs. The outcome of this review is a comprehensive taxonomy that categorizes PEFT usage by task type, distinguishing between generative (e.g., Code Summarization) and non-generative (e.g., Code Clone Detection) scenarios. Our findings aim to inform future research and guide the practical deployment of PEFT in sustainable, AI-powered software development.

---

## Visualizations

### 1. Heatmap of PEFT Methods Across Software Engineering Tasks

![PEFT Heatmap](visualizations/heatmap_of_peft_methods_across_se_tasks_v2.png)

- **Figure**: Number of studies using each PEFT method for each SE task.

### 2. SE Task Distribution Over Time

![Tasks by Year](visualizations/enhanced_se_task_trends_v2.png)

- Evolution of SE tasks targeted by PEFT research from 2022–2025.


### 3. Publication Venues

![Publication Venues](visualizations/venue_barplot_v2.png)

- Distribution of PEFT-SE research across conferences and journals.

### 4. Paper Selection Process

![Paper Selection Process](visualizations/data_collection_pipeline_v2.png)

- Workflow for paper selection in the SLR.

---

## Repository Structure

| Folder/File | Purpose |
|:------------|:--------|
| `/data` | Contains processed data and metadata for selected papers |
| `/scripts` | Scripts for data processing and visualization |
| `/visualizations` | All generated charts and plots |
| `README.md` | Updated README document |
| `requirements.txt` | Python dependencies |

---

## How to Reproduce

1. Clone the repository:
   ```bash
   git clone https://github.com/alvi75/SLR-PEFT.git
   cd SLR-PEFT
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run visualization scripts (optional):
   ```bash
   python scripts/venue_distribution.py
   ```

Outputs will be saved inside the `/visualizations` folder.

---

Thank you for exploring our work on PEFT for software engineering tasks!
