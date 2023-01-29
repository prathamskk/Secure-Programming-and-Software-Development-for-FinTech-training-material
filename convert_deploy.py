import os
import markdown
import requests

# Convert Markdown files to HTML
for file in os.listdir("markdown_files"):
    with open(f"markdown_files/{file}", 'r') as f:
        markdown_text = f.read()
    html = markdown.markdown(markdown_text)
    with open(f"html_files/{file}.html", 'w') as f:
        f.write(html)

# Commit and push changes to GitHub repository
url = "https://api.github.com/repos/username/repository_name/contents/html_files"

for file in os.listdir("html_files"):
    with open(f"html_files/{file}", 'rb') as f:
        file_data = f.read()
    sha = requests.get(url+'/'+file).json()['sha']
    data = {
        "message": "Update Blog",
        "content": file_data.hex(),
        "sha": sha
    }
    auth = ("username", "password_or_access_token")
    response = requests.put(url+'/'+file, json=data, auth=auth)
