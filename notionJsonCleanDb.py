with open("./data/jsonviewer.json", "r") as json_file:
    lines = json_file.readlines()

output_lines = []

for line in lines:
    if "^^^^" in line:
        output_lines.append(line.strip())

with open("output.txt", "w") as output_file:
    output_file.write('\n'.join(output_lines))