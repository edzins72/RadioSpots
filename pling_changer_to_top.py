import os

input_folder = r'D:\darbs\IT\Radio\TOP Radio\Traffic\RadioSpots\in'
output_folder = r'D:\darbs\IT\Radio\TOP Radio\Traffic\RadioSpots\out'
search_text_intro = "PLING INTRO"
search_text_id_in = 'SS11'
search_text_id_out = 'SS99'
replace_text_intro = "TOPintro"
search_text_outro = "PLING OUTRO"
replace_text_outro = "TOPoutro"
replace_id_in = 'SS12'
replace_id_out = 'SS100'

for file in os.listdir(input_folder):
    if os.path.isfile(os.path.join(input_folder, file)) and file.endswith(".2"):
        with open(os.path.join(input_folder, file), 'r') as f:
            data = f.read()
            data = data.replace(search_text_intro, replace_text_intro)
            data = data.replace(search_text_outro, replace_text_outro)
            data = data.replace(search_text_id_in, replace_id_in)
            data = data.replace(search_text_id_out, replace_id_out)

        with open(os.path.join(output_folder, file), 'w') as f:
            f.write(data)

        os.remove(os.path.join(input_folder, file))

print("Done")
