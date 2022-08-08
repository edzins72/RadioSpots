import os

input_folder = r'C:\Users\edgars\Documents\RadioSpots\traffic'
output_folder = r'C:\Users\edgars\Documents\RadioSpots\traffic_top'
search_text_intro = "PLING INTRO"
replace_text_intro = "TOPintro"
search_text_outro = "PLING OUTRO"
replace_text_outro = "TOPoutro"

for file in os.listdir(input_folder):
    if os.path.isfile(os.path.join(input_folder, file)) and file.endswith(".2"):
        with open(os.path.join(input_folder, file), 'r') as f:
            data = f.read()
            data = data.replace(search_text_intro, replace_text_intro)
            data = data.replace(search_text_outro, replace_text_outro)

        with open(os.path.join(output_folder, file), 'w') as f:
            f.write(data)

print("Done")
