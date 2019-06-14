import pandas as pd


def from_JSON_to_XLSX(input_path, output_path):
    pd.read_json(input_path, encoding='utf-8').to_excel(output_path, encoding='utf8')


from_JSON_to_XLSX("../data/dataset_human_vaccination.json", "../data/output.xlsx")
