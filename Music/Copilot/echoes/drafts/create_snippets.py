
import os

def save_snippet(snippet, filename):
    temp_folder = r'C:\Users\i3\Music\Copilot\echoes\drafts\temp'
    os.makedirs(temp_folder, exist_ok=True)
    file_path = os.path.join(temp_folder, filename)

    with open(file_path, 'w') as file:
        file.write(snippet)

    print(f"Snippet saved to: {file_path}")

def read_and_save_snippets(snippets_file):
    with open(snippets_file, 'r') as file:
        snippets = file.read().split('\n\n')  # Assuming snippets are separated by double newline

    for i, snippet in enumerate(snippets, start=1):
        save_snippet(snippet, f'temp_{i}.txt')

# Path to the snippets text file
snippets_file = r'C:\Users\i3\Music\Copilot\echoes\snippets.txt'

# Read and save snippets
read_and_save_snippets(snippets_file)
