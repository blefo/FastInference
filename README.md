# FastInference - The Really Fast LLM Querying API Manager (OpenAi, HuggingFace, Ollama, ...)

Call all LLM APIs and get the responses very fast with a **highly robust and distributed** library.
All the LLMs providers can be used with FastInference  [OpenAI, Huggingface, VertexAI, TogetherAI, Azure, etc.]

## Features

- **High Performance**: Get high inference speed thanks to intelligent asynchronous and distributed querying.
- **Robust Error Handling**: Advanced mechanisms to handle exceptions, ensuring robust querying.
- **Ease of Use**: Simplified API designed for working with all the LLM providers: easy and fast.
- **Scalability**: Optimized for large datasets and high concurrency.

## Usage

```bash
pip install fastllmquery
```

```python
from FastInference import FastInference

prompt = """
            You will be provided with a tweet, and your task is to classify its sentiment as positive, neutral, or negative.
            
            Tweet: {tweet_content}
        """

api_key = "you-api-key"
model_name = "modelprovider/model_name"

results = FastInference(file_path="your-dataset-file-path", 
                        main_column="your-main-feature", 
                        prompt=prompt, 
                        api_key=api_key,
                        model_name=model_name, 
                        only_response=True)
print(results)
```

### The Parameters
Here are the parameters that are not optional for initializing the FastInference object.
* **file_path** (string): path to your dataset (csv, xlsx, json, parquet)
* **main_column** (string): name of the main column (explained below in detail)
* **prompt** (string): the prompt with the variable in it (explained below in detail)
* **api_key** (string): your API key
* **model_name** (string): has the format provider/model_name (for example "huggingface/meta-llama/Meta-Llama-3-70B")
* **only_response** (bool): if True, you get a list containing the response of the LLM otherwise you get the full object normalized following the OpenAI API



### The Prompt
One of the parameter of the FastInference library is a prompt.The prompt must be in a string format.
It contains between curly brackets the column's name from your dataset where you want the variable to be in the prompt.

#### Example Usage
To understand how to use the `prompt` parameter in the FastInference library, we'll provide an example based on a tweet sentiment classification task. Consider a dataset with the following structure:

| tweet_content                                           | related_entities |
|---------------------------------------------------------|------------------|
| "Just had the best day ever at the NeurIPS Conference!" | "NeurIPS"        |
| "Traffic was terrible this morning in Paris."           | "Paris"          |
| "Looking forward to the new Star Wars movie!"           | "Star Wars"      |

One of the parameters of the FastInference library is a `prompt`. This must be formatted as a string. It contains, within curly brackets, the names of the columns from your dataset that you want to include in the prompt.

Here's how you could set up your prompt for classifying the sentiment of tweets based on their content and related entities:

```python
prompt = """
          You will be provided with a tweet, and your task is to classify its sentiment as positive, neutral, or negative.
          You must consider the related identified entities in order to make a good decision.
          
          Tweet: {tweet_content}
          Related Entities: {related_entities}
          """
```

### The main_column Parameter
The parameter main_column is the parameter that is considered as the most important information for inference.
It is a string containing the name of the most important column in your data.
It does not influence the LLM in inference since the prompt does not create hierarchical relationships between data.

**The main column has no influence on LLM inference.**


### Supported Providers ([Docs](https://docs.litellm.ai/docs/providers))

The FastInference is based on the open-source [LiteLLM](https://github.com/BerriAI/litellm/blob/main/README.md) library. All the supported LLMs by LiteLLM are also by FastInference.

| Provider                                                                            | [Completion](https://docs.litellm.ai/docs/#basic-usage) |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------- |
| [openai](https://docs.litellm.ai/docs/providers/openai)                             | ✅                                                      |
| [azure](https://docs.litellm.ai/docs/providers/azure)                               | ✅                                                      |
| [aws - sagemaker](https://docs.litellm.ai/docs/providers/aws_sagemaker)             | ✅                                                      |
| [aws - bedrock](https://docs.litellm.ai/docs/providers/bedrock)                     | ✅                                                      |
| [google - vertex_ai [Gemini]](https://docs.litellm.ai/docs/providers/vertex)        | ✅                                                      |
| [google - palm](https://docs.litellm.ai/docs/providers/palm)                        | ✅                                                      |
| [google AI Studio - gemini](https://docs.litellm.ai/docs/providers/gemini)          | ✅                                                      |
| [mistral ai api](https://docs.litellm.ai/docs/providers/mistral)                    | ✅                                                      |
| [cloudflare AI Workers](https://docs.litellm.ai/docs/providers/cloudflare_workers)  | ✅                                                      |
| [cohere](https://docs.litellm.ai/docs/providers/cohere)                             | ✅                                                      |
| [anthropic](https://docs.litellm.ai/docs/providers/anthropic)                       | ✅                                                      |
| [huggingface](https://docs.litellm.ai/docs/providers/huggingface)                   | ✅                                                      |
| [replicate](https://docs.litellm.ai/docs/providers/replicate)                       | ✅                                                      |
| [together_ai](https://docs.litellm.ai/docs/providers/togetherai)                    | ✅                                                      |
| [openrouter](https://docs.litellm.ai/docs/providers/openrouter)                     | ✅                                                      |
| [ai21](https://docs.litellm.ai/docs/providers/ai21)                                 | ✅                                                      |
| [baseten](https://docs.litellm.ai/docs/providers/baseten)                           | ✅                                                      |
| [vllm](https://docs.litellm.ai/docs/providers/vllm)                                 | ✅                                                      |
| [nlp_cloud](https://docs.litellm.ai/docs/providers/nlp_cloud)                       | ✅                                                      |
| [aleph alpha](https://docs.litellm.ai/docs/providers/aleph_alpha)                   | ✅                                                      |
| [petals](https://docs.litellm.ai/docs/providers/petals)                             | ✅                                                      |
| [ollama](https://docs.litellm.ai/docs/providers/ollama)                             | ✅                                                      |
| [deepinfra](https://docs.litellm.ai/docs/providers/deepinfra)                       | ✅                                                      |
| [perplexity-ai](https://docs.litellm.ai/docs/providers/perplexity)                  | ✅                                                      |
| [Groq AI](https://docs.litellm.ai/docs/providers/groq)                              | ✅                                                      |
| [anyscale](https://docs.litellm.ai/docs/providers/anyscale)                         | ✅                                                      |
| [IBM - watsonx.ai](https://docs.litellm.ai/docs/providers/watsonx)                  | ✅                                                      |
| [voyage ai](https://docs.litellm.ai/docs/providers/voyage)                          |                                                         |
| [xinference [Xorbits Inference]](https://docs.litellm.ai/docs/providers/xinference) |                                                         |

[**Read the Docs**](https://docs.litellm.ai/docs/)

