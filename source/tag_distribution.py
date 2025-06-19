import json

# Path to your JSON file
json_file = './tmp/tagData.json'  # Change this to your actual JSON file path

# Load data from JSON
with open(json_file, 'r') as f:
    data = json.load(f)

# Assume data is a dict: { "tag1": count1, "tag2": count2, ... }
# If your JSON structure is different, adjust accordingly.

# Prepare Mermaid pie chart block
mermaid_lines = ["\n\n\n","```mermaid", '---', 'config:', '    theme: "base"', 
                 '    themeVariables:', "      primaryColor: '#81c8be'", "      secondaryColor: '#e5c890'",  
                 "      tertiaryColor: '#8caaee'",
                 '---', "pie"]

for tag, count in data.items():
    mermaid_lines.append(f'    title ')
    break  # Only add title once

for tag, count in data.items():
    mermaid_lines.append(f'    "{tag}" : {count}')
mermaid_lines.append("```")

# Write to index.md
with open('./content/index.md', 'a+') as f:
    f.write('\n'.join(mermaid_lines) + '\n')