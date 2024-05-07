from FastInference import FastInference

if __name__ == '__main__':
    results = FastInference(
        r"C:\Users\baptiste.lefort\Documents\final_results\perimeter_headlines.xlsx",
        "Title",
        "This is the context: {content} with value {Date}",
    ).run()

    print(results)
