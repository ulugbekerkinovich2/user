import json
from transliterate import translit

# Open the JSON file with UTF-8 BOM handling
# with open('C:/Users/ulugbek/Downloads/fanlar_majmuasi.json', 'r', encoding='utf-8-sig') as file:
#     data = json.load(file)
#
# # Convert the Cyrillic text to Latin script
# converted_data = []
# for item in data:
#     converted_item = {}
#     for key, value in item.items():
#         converted_key = translit(key, 'ru', reversed=True)
#         converted_value = translit(value, 'ru', reversed=True)
#         converted_item[converted_key] = converted_value
#     converted_data.append(converted_item)
#
# # Save the converted data to a new JSON file
# with open('fanlar_majmuasi_output.json', 'w', encoding='utf-8') as file:
#     json.dump(converted_data, file, indent=4, ensure_ascii=False)


with open('fanlar_majmuasi_output.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

for obj in data:
    print(obj)