# Meet the Machines: Ollama, Hugging Face, and Critical Comparison

## Overview
This lab focuses on the initial setup and exploration of Ollama and Hugging Face. Ollama is a free, open-source platform used to download, run, and manage large language models (LLMs) directly on a local computer, while Hugging Face is an open-source platform and central hub for discovering, sharing, training, and deploying AI and machine learning models.

The lab helps us understand how to read model cards and select suitable models based on available computing resources, memory, and processing power. We also compare different models using the same prompts and observe how their responses change when the audience, role, and format of the prompt change. In addition, we test the reliability of model outputs by verifying factual claims, checking citations and research papers, and reviewing generated code. 

Finally, the lab highlights the importance of verifying AI-generated information, especially when using it for research or other important work.


## Step 1: Install and verify Ollama
| Field                                | Your answer                    | 
| ------------------------------------ | ------------------------------ |
| Model pulled                         | llama3.2                       |
| Time to first reply (seconds, rough) |less than a second              |
| Screenshot filename                  |screenshots/llama_working.png  |


## Step 2: Explore Hugging Face like an engineer
| Field | Model 1 | Model 2 | Model 3 |
|---|---|---|---|
| Full name and URL | meta-llama/Llama-3.2-3B-Instruct<br>https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct | mistralai/Mistral-7B-Instruct-v0.3<br>https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 | Qwen/Qwen2.5-1.5B-Instruct<br>https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct |
| Parameters (e.g. 3B, 7B) | 3B | 7B | 2B |
| License (e.g. Apache 2.0, Llama, MIT) | Llama 3.2 Community License | Apache 2.0 | Apache 2.0 |
| Intended use (from card) | Commercial and research use; assistant-like chat, agentic applications, knowledge retrieval, summarization, mobile AI-powered writing assistants, query and prompt rewriting, and other natural language generation tasks. | It is an instruct fine-tuned version of the Mistral-7B-v0.3, trained to understand and follow direct user commands, conversational prompts, and tasks like summarization | Instruction-following tasks, chat, long-text generation, structured data understanding, structured output generation, coding, mathematics, and multilingual applications. |
| Known limitations | Testing has not covered all possible scenarios, so Llama 3.2’s outputs cannot be predicted in advance. It may produce inaccurate, biased, or otherwise objectionable responses. Developers should perform safety testing and tuning for their specific applications before deployment. | Does not have any moderation mechanisms. Working on ways to make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs. | Requires a recent version of Transformers. The model has a 32K-token context length and 8K-token generation limit. |
| Languages supported | English, German, French, Italian, Portuguese, Hindi, Spanish, Thai | Primarily English, multilingual capability is not stated. | Over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic and more |
| Available on Ollama? (yes/no/check library) | Yes (llama3.2:3b) | Yes (mistral:7b-instruct) | Yes (qwen2.5:1.5b-instruct) |


### Questions
1. Which model would you not use in a commercial product? Quote the license line that supports your answer:

All 3 models can be used for commercial purposes. In the Llama intended use cases it cleary states Llama 3.2 is intended for commercial and research use in multiple languages (License Rights and Redistribution. Grant of Rights. You are granted a non-exclusive, worldwide, non-transferable and royalty-free limited license under Meta’s intellectual property or other rights 
owned by Meta embodied in the Llama Materials to use, reproduce, distribute, copy, create derivative works 
of, and make modifications to the Llama Materials.). While Mistral and Qwen have the Apache 2.0 licence which allows for unrestricted commercial use. (Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.)

2. Which model fits a student laptop best for local experiments? Why?:

Qwen2.5-1.5B-Instruct fits best because it has only 1.54B parameters and 986 MB in size, which makes it the smallest of the three models. A smaller model generally requires fewer computing resources, memory and processing power needed to run or train it.

3. What is one risk mentioned in a model card that you had not thought about before?:

Llama 3.2’s potential outputs cannot be predicted in advance and it may produce inaccurate, biased, or otherwise objectionable responses. I'm wondering how reliable that makes it if it's behaviour is unpredictable.
It also mentioned the model is supposed to be deployed as part of an overall AI system with additional safety guardrails as required and it is the developers responsibility to ensure that. Is that what people see as the AI model going rogue? When safety guardrails are not enforced by developers?


## Step 3: The same prompt experiment
| Run | System | Model name (exact tag) |
|---|---|---|
| A | Ollama | llama3.2 |
| B | Ollama (different model) | mistral:7b-instruct |
| C | Third system | qwen2.5:1.5b-instruct |

**Prompt**:
Explain overfitting in machine learning using a real-world analogy. Include one sentence on how to reduce it. Keep the answer under 150 words.

**Score card**:
Run A = 3 secs
Run B = 4 secs
Run C = 1 sec

| Criterion                         | Run A | Run B | Run C |
|-----------------------------------|-------|-------|-------|
| Accuracy (is the ML idea correct?) |  5     |   5    |    3   |
| Clarity (would a classmate understand?) |   5    |    5   |   4    |
| Completeness (analogy + reduction tip?) |   5    |    5   |    4   |
| Respects ~150 word limit          |   5    |   5    |   5   | 
| Overall                           |   20    |    20   |   16   |

Best model(Run B) - mistral:7b-instruct - the clarity and accuracy with how it explained overfitting. It explained the poor performance on unseen data clearly and gave an explanation on how increasing the training data helps with reducing overfitting.


## Step 4: Audience shift experiment - usinf the best model
| Prompt | What changed besides vocabulary? | New factual claim? | Trust it? |
|---|---|---|---|
| Child | Simplifies the explanation but still sounds high level for a 12 year old. | No new factual claim. | Yes |
| Student | Adds specific techniques for avoiding overfitting like cross-validation, regularization, and simpler models. | Yes new factual claims about how to reduce ovefitting | Yes |
| Researcher | Adds the bias-variance tradeoff, explains bias, variance | Yes. It introduces additional factual technical claims. | Yes |


For the child response (outputs/step4_child.txt) I will change "In machine learning, a model can learn too much from the training data and perform poorly on new, unseen data.It's important to find a balance so the model can learn well but not too much"  to "The goal is to focus on the general features instead of highlighting every little detail." which follows the drawing analogy and substitutes all the technical words for everyday language for a 12 year old.


## Step 5: Reliability and hallucination hunt
Verifiable fact test

| Model output | Your verification source | Verdict (correct / incorrect / ambiguous) |
|---|---|---|
|  Canberra  | Google | correct |


Citation trap

| Title (as model gave it) | Exists? | Authors match? | Notes |
|---|---|---|---|
| Attention is All You Need  | Yes | All but 1  | S. Tenenbaum is not an authur on this paper |
| Transformer-XL: Longer, Faster, Better Models for Long Sequences | Yes but the title is incorrect | No | Title is Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context and the authurs are Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V. Le, and Ruslan Salakhutdinov |
| RoBERTA: A Robustly Optimized BERT Pretraining Approach | Yes | All but 1 | The correct name is Veselin Stoyanov not Mark Neumann |


Code sanity check

| Check | Result |
|---|---|
| Runs without syntax error? | Yes |
| Formula looks correct? | Yes |
| Any invented NumPy functions? | No |


## Step 6: Toolchain reflection
1. Ollama:

What worked well?: I could test models such as Llama, Mistral, and Qwen locally and run comparisons on their outputs easily based on certain prompts.
What frustrated you?: I couldn't immediately find the models I was reviewing on Hugging face on Ollama. Especially when trying to find the exact versions.

2. Hugging Face: What would you check before using a model in a client project?

I would check its license to make sure commercial use is allowed. I would also check the model's intended use, limitations, supported languages, and parameter size. I would review the model card to understand how the model was trained and any known risks or limitations. I would also test the model with relevant data to see whether its performance is suitable for the project.

3. Modal (conceptual): Describe one task from this lab that would not run well on your laptop but would need a cloud GPU.

Running or fine-tuning a large language model. Larger models require a lot of memory and computing power, especially when training or fine-tuning them. A cloud GPU would provide the processing power and memory needed to run the model efficiently. Allowing the task to complete much faster than it would on my laptop.

4. Trust:  

Under what conditions would you trust output from your local Ollama model without verification?: When it is being used for simple tasks such as brainstorming, rewriting text, explaining basic concepts that I already understand or if I asked the model for an opinion.  
Under what conditions would you never?: For important factual information I would always verify the output against reliable sources. Example for medical, legal, financial, any information where specific facts, statistics, citations, claims are provided or for any other high-stakes decisions.


## Defrief
The models (Llama, Qwen, Mistral) when answering general knowledge questions and definitions of data science concepts were more factual, except Qwen that was confident in explaining techniques for reducing overfitting when it was wrong. But when asked to cite research papers Mistral started to hallucinate with the names of authurs and titles of the research papers.
When working with AI-generated text about content I am not sure of I will always verify because I could have made reference to research papers that didn't exist in important school work or research of my own.