import pandas as pd


def from_JSON_to_XLSX(input_path, output_path):
    pd.read_json(input_path).to_excel(output_path)


from_JSON_to_XLSX("../data/dataset_human_vaccination.json", "../data/output.xlsx")
