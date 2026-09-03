## Step 1: Install and verify Ollama

| Field                                | Your answer       | 
| ------------------------------------ | ----------------- |
| Model pulled                         | llama3.2          |
| Time to first reply (seconds, rough) |less than a second |
| Screenshot filename                  |                   |



## Step 2: Explore Hugging Face like an engineer


| Field | Model 1 | Model 2 | Model 3 |
|---|---|---|---|
| Full name and URL | meta-llama/Llama-3.2-3B-Instruct<br>https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct | mistralai/Mistral-7B-Instruct-v0.3<br>https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 | Qwen/Qwen2.5-1.5B-Instruct<br>https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct |
| Parameters (e.g. 3B, 7B) | 3B | 7B | 2B |
| License (e.g. Apache 2.0, Llama, MIT) | Llama 3.2 Community License | Apache 2.0 | Apache 2.0 |
| Intended use (from card) | Commercial and research use; assistant-like chat, agentic applications, knowledge retrieval, summarization, mobile AI-powered writing assistants, query and prompt rewriting, and other natural language generation tasks. | It is an instruct fine-tuned version of the Mistral-7B-v0.3. | Instruction-following tasks, chat, long-text generation, structured data understanding, structured output generation, coding, mathematics, and multilingual applications. |
| Known limitations | Testing has not covered all possible scenarios, so Llama 3.2’s outputs cannot be predicted in advance. It may produce inaccurate, biased, or otherwise objectionable responses. Developers should perform safety testing and tuning for their specific applications before deployment. | Does not have any moderation mechanisms. Working on ways to make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs. | Requires a recent version of Transformers. The model has a 32K-token context length and 8K-token generation limit. |
| Languages supported | English, German, French, Italian, Portuguese, Hindi, Spanish, Thai | Primarily English, multilingual capability is not stated. | Over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic and more |
| Available on Ollama? (yes/no/check library) | Yes (llama3.2:3b) | Yes (mistral:7b-instruct) | Yes (qwen2.5:1.5b-instruct) |


### Questions
1. Which model would you not use in a commercial product? Quote the license line that supports your answer.
All 3 models can be used for commercial purposes. In the Llama intended use cases it cleary states Llama 3.2 is intended for commercial and research use in multiple languages (License Rights and Redistribution. Grant of Rights. You are granted a non-exclusive, worldwide, non-transferable and royalty-free limited license under Meta’s intellectual property or other rights 
owned by Meta embodied in the Llama Materials to use, reproduce, distribute, copy, create derivative works 
of, and make modifications to the Llama Materials.). While Mistral and Qwen have the Apache 2.0 licence which allows for unrestricted commercial use. (Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.)

2. Which model fits a student laptop best for local experiments? Why?
Qwen2.5-1.5B-Instruct fits best because it has only 1.54B parameters which makes it the smallest of the three models. A smaller model generally requires fewer computing resources

3. What is one risk mentioned in a model card that you had not thought about before?
Llama 3.2’s potential outputs cannot be predicted in advance. I'm wondering how reliable that makes it.


## Step 3: The same prompt experiment
| Run | System | Model name (exact tag) |
|---|---|---|
| A | Ollama | llama3.2 |
| B | Ollama (different model) | mistral:7b-instruct |
| C | Third system | qwen2.5:1.5b-instruct |


Run A was the fastest, followed by B and C

| Criterion                         | Run A | Run B | Run C |
|-----------------------------------|-------|-------|-------|
| Accuracy (is the ML idea correct?) |  4     |   5    |    5   |
| Clarity (would a classmate understand?) |   5    |    5   |   4    |
| Completeness (analogy + reduction tip?) |   5    |    5   |    5   |
| Respects ~150 word limit          |   5    |   5    |   5   |
| Overall                           |   19    |    20   |   19    |


## Step 4: Audience shift experiment
Best model - mistral:7b-instruct 
| Prompt | What changed besides vocabulary? | New factual claim? | Trust it? |
|---|---|---|---|
| Child | Simplifies the explanation and uses a student/test-book analogy. It also adds the idea of finding a balance when fitting the data. | No significant new factual claim. | Yes |
| Student | Adds specific techniques for avoiding overfitting: cross-validation, regularization, and simpler models. | Yes. These are factual claims about techniques used to reduce overfitting. | Yes |
| Researcher | Adds the bias-variance tradeoff, explains bias, variance, and irreducible error, and suggests collecting more diverse data to reduce variance. | Yes. It introduces several additional technical claims. | Mostly yes, but the claim that irreducible error is simply “noise in the data” is an oversimplification. |
