# Repository README.md
This repository contains a solution for the problem of cleaning up unnecessary databases and backups that have accumulated over time. The approach used involves pulling all databases in one list using a semi-manual method, since API requests failed to provide the necessary information.

# Problem
When there is an accumulation of more than 500+ databases and in total more than 40K+ automatic or manual backups are done for it over 3 hours. It is obvious that too many unnecessary databases and garbage have accumulated, which need to be viewed as a single list for further cleaning and deletion. Because of their number it is too long and the idea came up to the optimization of pulling all databases in one list. Unfortunately, all attempts to do so through API requests were unsuccessful due to the deprecation of v1 and v2 methods.

# Solution
The following semi-manual method was used to obtain a list of all databases:

Create a new database and select from the list of existing ones. The Network search query will return a JSON with a list of all databases. Keep pressing "view 20 more" until all databases are loaded and the last search JSON is the list of all databases.

Use https://codebeautify.org/jsonviewer to beautify the structure and re-save to a file manually.
You'll get 3+mb json for i.e. in my case
```
...
"8e07fc21-f6c1-4d0f-8c81-43cffa5acaac": {
        "spaceId": "03f65aef-1955-4889-8eda-5f43cd979692",
        "value": {
          "role": "editor",
          "value": {
            ^^^^"id": "8e07fc21-f6c1-4d0f-8c81-43cffa5acaac",
            "version": 21,
            "name": [
              [
                "DeprecatedSprints"^^^^
              ]
            ],
            "schema": {
              ":b=s": {
                "name": "Year",
                "type": "select",
                "options": [
                  {
                    "id": "ecad8f65-daa0-476b-8fe6-83b12ab99200",
                    "color": "green",
                    "value": "2020"
                  },
                  {
                    "id": "6e94f43e-b24a-41a1-b8da-5f3dc88af613",
                    "color": "brown",
                    "value": "2021"
                  }
                ]
              },
...
```

Add the special characters ^^^^ at the beginning of each line for databases and at the end of the header through standard search & replaces. You'll get something like this.
```
...
"role": "editor",
          "value": {
            ^^^^"id": "8e07fc21-f6c1-4d0f-8c81-43cffa5acaac",
            "version": 21,
            "name": [
              [
                "DeprecatedSprints"^^^^
              ]
            ],
            "schema": {
...
```

Write a Python script to parse the file and extract the necessary entries, saving them to a .txt file. The script used is as follows:

python
Copy code
with open("./data/jsonviewer.json", "r") as json_file:
    lines = json_file.readlines()

output_lines = []

for line in lines:
    if "^^^^" in line:
        output_lines.append(line.strip())

with open("output.txt", "w") as output_file:
    output_file.write('\n'.join(output_lines))
Manually convert the output.txt file to .csv format using search & replace. The resulting file should have the following format:

bash
Copy code
id,title-of-database
8e07fc21-f6c1-4d0f-8c81-43cffa5acaac,DeprecatedSprints
8ed4e2d2-7df7-4905-a09d-1876f260e56b,Competitive Landscape
This method provides a workable solution for obtaining a list of all databases in order to clean up unnecessary ones.

Usage
This repository provides the Python script used to parse the jsonviewer.json file and extract the necessary entries, as well as an example output.txt file. To use the script, simply run it in a Python environment with the jsonviewer.json file in the ./data directory. The script will output a output.txt file in the same directory with the necessary entries.

Contributing
Feel free to contribute to this repository by creating pull requests or opening issues.

When contributing, please follow the best practices and guidelines for contributing to open-source projects.

License
This repository is licensed under the MIT license. See the LICENSE file for details.