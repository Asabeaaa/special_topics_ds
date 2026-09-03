
| Field                                | Your answer       | 
| ------------------------------------ | ----------------- |
| Model pulled                         | llama3.2          |
| Time to first reply (seconds, rough) |less than a second |
| Screenshot filename                  |                   |



| Field | Model 1 | Model 2 | Model 3 |
|---|---|---|---|
| Full name and URL | meta-llama/Llama-3.2-3B-Instruct<br>https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct | mistralai/Mistral-7B-Instruct-v0.3<br>https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 | Qwen/Qwen2.5-1.5B-Instruct<br>https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct |
| Parameters (e.g. 3B, 7B) | 3B | 7B | 1.54B |
| License (e.g. Apache 2.0, Llama, MIT) | Llama 3.2 Community License | Apache 2.0 | Apache 2.0 |
| Intended use (from card) | Commercial and research use; assistant-like chat, agentic applications, knowledge retrieval, summarization, mobile AI-powered writing assistants, query and prompt rewriting, and other natural language generation tasks. | Instruction following, chat, and function calling. It is an instruction-fine-tuned version of Mistral-7B-v0.3. | Instruction-following tasks, chat, long-text generation, structured data understanding, structured output generation, coding, mathematics, and multilingual applications. |
| Known limitations | May produce inaccurate, biased, or objectionable responses. Testing does not cover all possible scenarios. Use is restricted to supported languages and applicable license/use policies. | Does not have built-in moderation mechanisms and may require additional guardrails for moderated deployments. | Requires a recent version of Transformers. The model has a 32K-token context length and 8K-token generation limit. |
| Languages supported | English, German, French, Italian, Portuguese, Hindi, Spanish, Thai | Primarily English; multilingual capability is not a stated focus of this model card. | Over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, and Arabic. |
| Available on Ollama? (yes/no/check library) | Yes (`llama3.2:3b`) | Yes (`mistral:7b-instruct`) | Yes (`qwen2.5:1.5b-instruct`) |

