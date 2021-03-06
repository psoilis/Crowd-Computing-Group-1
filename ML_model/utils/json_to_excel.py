import pandas as pd


def from_JSON_to_XLSX(input_path, output_path):
    writer = pd.ExcelWriter(path=output_path, engine='xlsxwriter', options={'strings_to_numbers': False,
                                                                            'strings_to_urls': False})
    pd.read_json(input_path, dtype='str', encoding='utf-8').to_excel(writer, encoding='utf-8', index=False)
    writer.save()


from_JSON_to_XLSX(input_path="../data/dataset_human_vaccination_subsample.json",
                  output_path="../data/figure8_dataset.xlsx")
