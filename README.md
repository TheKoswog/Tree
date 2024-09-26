How It Works
Traversing Directories: The tree walks through the directories and subdirectories starting from the current working directory.
Writing to a File: The directory structure is written to the directory_tree.txt file, maintaining the hierarchy using indentation.
Tree Structure: Folders and files are displayed using tree-like symbols (├── for items and │ for indentation).
Output Example
If the current directory contains the following structure:

bash
/my_project
├── tree.py
├── folder1/
│   ├── file1.txt
│   ├── file2.txt
└── folder2/
    └── file3.txt
The tree will output the following in the directory_tree.txt file:

bash
/my_project
├── tree.py
├── folder1/
│   ├── file1.txt
│   ├── file2.txt
└── folder2/
    └── file3.txt
Usage
Run the tree by executing python tree.py in the terminal.
After execution, you will find the directory_tree.txt file in the current directory, containing the directory tree structure.
