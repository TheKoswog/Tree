import os

def write_directory_tree(startpath, output_file, indent_level=0):
    for item in os.listdir(startpath):
        item_path = os.path.join(startpath, item)
        indent = '│   ' * indent_level + '├── ' if indent_level > 0 else ''
        
        if os.path.isdir(item_path):
            output_file.write(f"{indent}{item}/\n")
            write_directory_tree(item_path, output_file, indent_level + 1)
        else:
            output_file.write(f"{indent}{item}\n")

# Get the current working directory
root_directory = os.getcwd()

# Name of the output file
output_file_path = "directory_tree.txt"

# Write the directory tree to a text file
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(f"{root_directory}\n")
    write_directory_tree(root_directory, output_file)

print(f"Directory tree saved to '{output_file_path}'")
