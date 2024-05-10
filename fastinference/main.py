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

    api_key = "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"
    model_name = "huggingface/google/gemma-1.1-7b-it"

    # api_key = "your-azure-key"
    # model = "azure/your-azure-model"
    # api_base = "your-azure-endpoint"
    # api_version = "your-azure-api-version"

    results = FastInference(
        file_path=r"C:\Users\baptiste.lefort\Documents\final_results\perimeter_headlines.xlsx",
        main_column="Title",
        prompt=prompt,
        api_key=api_key,
        model=model_name
    ).run()

    print(results)
