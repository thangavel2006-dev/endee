import requests

def get_repo_files(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    response = requests.get(url)

    files = []

    for item in response.json():
        if item["type"] == "file":
            files.append(item["download_url"])

    return files


def get_file_content(url):
    return requests.get(url).text


def chunk_text(text, chunk_size=300):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks