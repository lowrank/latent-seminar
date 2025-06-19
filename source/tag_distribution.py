import json
import os
import re

# Path to your JSON file
json_file = './tmp/tagData.json'  # Change this to your actual JSON file path

# Load data from JSON
with open(json_file, 'r') as f:
    data = json.load(f)

# Assume data is a dict: { "tag1": count1, "tag2": count2, ... }
# If your JSON structure is different, adjust accordingly.

# Prepare Mermaid pie chart block
mermaid_lines = ["```mermaid", '---', 'config:', '    theme: "base"', 
                 '    themeVariables:', "      primaryColor: '#81c8be'", "      secondaryColor: '#e5c890'",  
                 "      tertiaryColor: '#8caaee'",
                 '---', "pie"]

for tag, count in data.items():
    mermaid_lines.append(f'    title ')
    break  # Only add title once

for tag, count in data.items():
    mermaid_lines.append(f'    "{tag}" : {count}')
mermaid_lines.append("```")


# Read existing content if index.md exists

index_md_path = './content/index.md'
if os.path.exists(index_md_path):
    with open(index_md_path, 'r') as f:
        content = f.read()
    # Find existing mermaid block
    mermaid_pattern = re.compile(r'```mermaid.*?```', re.DOTALL)
    if mermaid_pattern.search(content):
        # Replace existing mermaid block
        content = mermaid_pattern.sub('\n'.join(mermaid_lines), content)
    else:
        # Append new mermaid block
        content += '\n' + '\n'.join(mermaid_lines) + '\n'
    with open(index_md_path, 'w') as f:
        f.write(content)
else:
    # If file doesn't exist, just write the mermaid block
    with open(index_md_path, 'w') as f:
        f.write('\n'.join(mermaid_lines) + '\n')