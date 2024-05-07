# MAmmoTH2

Instruction tuning improves the reasoning abilities of large language models (LLMs), with data quality and scalability being the crucial factors. Most instruction tuning data come from human crowd-sourcing or GPT-4 distillation. We propose a paradigm to efficiently harvest 10 million naturally existing instruction data from the pre-training web corpus to enhance LLM reasoning. Our approach involves (1) recalling relevant documents, (2) extracting instruction-response pairs, and (3) refining the extracted pairs using open-source LLMs. Fine-tuning base LLMs on this dataset, we build MAmmoTH2 models, which significantly boost performance on reasoning benchmarks. Notably, MAmmoTH2-7B’s (Mistral) performance increases from 11% to 34% on MATH and from 36% to 67% on GSM8K without training on any in-domain data. Further training MAmmoTH2 on public instruction tuning datasets yields MAmmoTH2-Plus, achieving state-of-the-art performance on several reasoning and chatbot benchmarks. Our work demonstrates how to harvest large- scale, high-quality instruction data without costly human annotation or GPT-4 distillation, providing a new perspective on building better instruction tuning data.

<p align="center">

<div style="display: flex; justify-content: center;">
    <img src="https://tiger-ai-lab.github.io/MAmmoTH2/static/images/teaser_front.jpg" style="height:300px; width:auto; margin-right:10px">
</div>
</p>

## WEBINSTRUCT
Reasoning is crucial for problem-solving and advancing knowledge. While large language models (LLMs) have made strides in natural language processing (NLP), their ability in complex reasoning tasks remains limited. Efforts to enhance LLMs' reasoning include continued training on filtered documents and instruction tuning with supervised fine-tuning loss. However, datasets for instruction tuning are often limited and biased, prompting a need for scalable and diverse instruction data.

To address this, we propose discovering instruction data from the web. We argue that vast amounts of high-quality instruction data exist in the web corpus, spanning various domains like math and science. Our three-step pipeline involves recalling documents from Common Crawl, extracting Q-A pairs, and refining them for quality. This approach yields 10 million instruction-response pairs, offering a scalable alternative to existing datasets.

Validating our dataset's effectiveness, we trained models on various base models, significantly outperforming them on seven reasoning benchmarks. Further tuning on open-source instruction datasets enhances performance, showcasing strong generalization abilities. Our approach demonstrates cost-effectiveness compared to human-annotated datasets, offering promising results for future instruction tuning studies.

<p align="center">

<div style="display: flex; justify-content: center;">
    <img src="https://tiger-ai-lab.github.io/MAmmoTH2/static/images/teaser.jpg" width:auto; margin-right:10px">
</div>
</p>

## Model Downloads

<div align="center">

| **Model**            | **Dataset**                                            | **Download**   |
| :------------:       | :------------:                                         | :------------: |
| MAmmoTH2-8x7B        | WebInstruct                                            | [🤗 HuggingFace](https://huggingface.co/TIGER-Lab/MAmmoTH2-8x7B)   |
| MAmmoTH2-8x7B        | WebInstruct                                            | [🤗 HuggingFace](https://huggingface.co/TIGER-Lab/MAmmoTH2-34B)   |
| MAmmoTH2-7B          | WebInstruct                                            | [🤗 HuggingFace](https://huggingface.co/TIGER-Lab/MAmmoTH2-7B)   |
| MAmmoTH2-8B          | WebInstruct                                            | [🤗 HuggingFace](https://huggingface.co/TIGER-Lab/MAmmoTH2-8B)   |
| MAmmoTH2-8x7B-Plus   | WebInstruct + OpenHermes2.5 + CodeFeedback + Math-Plus | [🤗 HuggingFace](https://huggingface.co/TIGER-Lab/MAmmoTH2-8x7B-Plus)   |
| MAmmoTH2-7B-Plus     | WebInstruct + OpenHermes2.5 + CodeFeedback + Math-Plus | [🤗 HuggingFace](https://huggingface.co/TIGER-Lab/MAmmoTH2-7B-Plus)   |
| MAmmoTH2-8B-Plus     | WebInstruct + OpenHermes2.5 + CodeFeedback + Math-Plus | [🤗 HuggingFace](https://huggingface.co/TIGER-Lab/MAmmoTH2-8-Plus)   |

</div>

## Evaluation Results

For the 20B+ models:
| Model                   | TheoremQA | MATH | GSM8K | GPQA | MMLU-ST | BBH  | ARC-C | Avg  |
|-------------------------|-----------|------|-------|------|---------|------|-------|------|
| GPT-4-Turbo-0409        | 48.4      | 69.2 | 94.5  | 46.2 | 76.5    | 86.7 | 93.6  | 73.6 |
| Qwen-1.5-110B           | 34.9      | 49.6 | 85.4  | 35.9 | 73.4    | 74.8 | 91.6  | 63.6 |
| Qwen-1.5-72B            | 29.3      | 46.8 | 77.6  | 36.3 | 68.5    | 68.0 | 92.2  | 59.8 |
| Deepseek-LM-67B         | 25.3      | 15.9 | 66.5  | 31.8 | 57.4    | 71.7 | 86.8  | 50.7 |
| Yi-34B                  | 23.2      | 15.9 | 67.9  | 29.7 | 62.6    | 66.4 | 89.5  | 50.7 |
| Llemma-34B              | 21.1      | 25.0 | 71.9  | 29.2 | 54.7    | 48.4 | 69.5  | 45.7 |
| Mixtral-8×7B            | 23.2      | 28.4 | 74.4  | 29.7 | 59.7    | 66.8 | 84.7  | 52.4 |
| Mixtral-8×7B-Instruct   | 25.3      | 22.1 | 71.7  | 32.4 | 61.4    | 57.3 | 84.7  | 50.7 |
| Intern-Math-20B         | 17.1      | 37.7 | 82.9  | 28.9 | 50.1    | 39.3 | 68.6  | 46.4 |
| MAmmoTH2-34B            | 30.4      | 35.0 | 75.6  | 31.8 | 64.5    | 68.0 | 90.0  | 56.4 |
| MAmmoTH2-8x7B           | 32.2      | 39.0 | 75.4  | 36.8 | 67.4    | 71.1 | 87.5  | 58.9 |
| MAmmoTH2-8x7B-Plus      | 34.1      | 47.0 | 86.4  | 37.8 | 72.4    | 74.1 | 88.4  | 62.9 |

For the 7B/8B-scale models:
| Model                   | TheoremQA | MATH | GSM8K | GPQA | MMLU-ST | BBH  | ARC-C | Avg  |
|-------------------------|-----------|------|-------|------|---------|------|-------|------|
| Deepseek-7B             | 15.7      | 6.4  | 17.4  | 25.7 | 43.1    | 42.8 | 47.8  | 28.4 |
| Qwen-1.5-7B             | 14.2      | 13.3 | 54.1  | 26.7 | 45.4    | 45.2 | 75.6  | 39.2 |
| Mistral-7B              | 19.2      | 11.2 | 36.2  | 24.7 | 50.1    | 55.7 | 74.2  | 38.8 |
| Gemma-7B                | 21.5      | 24.3 | 46.4  | 25.7 | 53.3    | 57.4 | 72.5  | 43.0 |
| Llemma-7B               | 17.2      | 18.0 | 36.4  | 23.2 | 45.2    | 44.9 | 50.5  | 33.6 |
| WizardMath-7B-1.1       | 11.7      | 33.0 | 83.2  | 28.7 | 52.7    | 56.7 | 76.9  | 49.0 |
| OpenMath-Mistral        | 13.1      | 9.1  | 24.5  | 26.5 | 43.7    | 49.5 | 69.4  | 33.7 |
| Abel-7B-002             | 19.3      | 29.5 | 83.2  | 30.3 | 29.7    | 32.7 | 72.5  | 42.5 |
| Intern-Math-7B          | 13.2      | 34.6 | 78.1  | 22.7 | 41.1    | 48.1 | 59.8  | 42.5 |
| Rho-1-Math-7B           | 21.0      | 31.0 | 66.9  | 29.2 | 53.1    | 57.7 | 72.7  | 47.3 |
| Deepseek-Math-7B        | 25.3      | 34.0 | 64.2  | 29.2 | 56.4    | 59.5 | 67.8  | 48.0 |
| Deepseek-Math-Instruct  | 23.7      | 44.3 | 82.9  | 31.8 | 59.3    | 55.4 | 70.1  | 52.5 |
| Llama-3-8B              | 20.1      | 21.3 | 54.8  | 27.2 | 55.6    | 61.1 | 78.6  | 45.5 |
| Llama-3-8B-Instruct     | 22.8      | 30.0 | 79.5  | 34.5 | 60.2    | 66.0 | 80.8  | 53.4 |
| MAmmoTH2-7B             | 26.7      | 34.2 | 67.4  | 34.8 | 60.6    | 60.0 | 81.8  | 52.2 |
| MAmmoTH2-8B             | 29.7      | 33.4 | 67.9  | 38.4 | 61.0    | 60.8 | 81.0  | 53.1 |
| MAmmoTH2-7B-Plus        | 29.2      | 45.0 | 84.7  | 36.8 | 64.5    | 63.1 | 83.0  | 58.0 |
| MAmmoTH2-8B-Plus        | 32.5      | 42.8 | 84.1  | 37.3 | 65.7    | 67.8 | 83.4  | 59.1 |

## Evaluation Command
Coming soon!
