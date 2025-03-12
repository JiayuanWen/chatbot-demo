import pandas
import ast

def generate_weekly_financial_report(data: list[dict]) -> None:
    report = ast.literal_eval(data)

    df = pandas.DataFrame(report)
    df.to_csv('output.csv', index=False)

    return "Report has been generated and saved to your working directory."