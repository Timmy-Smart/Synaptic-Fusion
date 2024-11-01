
import os

def compile_story(temp_folder, final_file):
    with open(final_file, 'w') as final:
        for filename in sorted(os.listdir(temp_folder)):
            temp_path = os.path.join(temp_folder, filename)
            if os.path.isfile(temp_path):
                with open(temp_path, 'r') as temp:
                    final.write(temp.read())
                    final.write("\n")

    print(f"Compiled story saved to: {final_file}")

# Define the paths
temp_folder = 'C:\Users\i3\Music\Copilot\echoes\drafts\temp'
final_file = 'C:\Users\i3\Music\Copilot\echoes\drafts\story_001.txt'

compile_story(temp_folder, final_file)
