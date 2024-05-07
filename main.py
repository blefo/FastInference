from FastInference import FastInference

if __name__ == '__main__':
    prompt = """
        You are given a financial headline and your task is to assess the impact of various economic events and trends on global equities.
        For the statement provided below, classify its impact as either "positive," "negative," or "indecisive".
        Write your answer on the next line following each statement, and only use one of the given words: "positive," "negative," "indecisive."
        Your response should be a single word among [-positive, -indecisive, -negative] with a "-" before the word.
        Here is the statement: {content}
        ANSWER:
    """

    api_key = "you-key"
    model_name = "huggingface/meta-llama/Meta-Llama-3-70B-Instruct"

    results = FastInference(
        file_path=r"C:\Users\baptiste.lefort\Documents\final_results\perimeter_headlines.xlsx",
        main_column="Title",
        prompt=prompt,
        api_key=api_key,
        model_name=model_name
    ).run()

    print(results)
