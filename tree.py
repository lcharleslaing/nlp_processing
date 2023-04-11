import os


def build_tree(dir_path, depth=0):
    tree = ""
    ignore_dirs = ['gpt_token_saver_env', 'build', '__pycache__']
    has_relevant_files = False
    for file in sorted(os.listdir(dir_path)):
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            if file in ignore_dirs:
                continue
            sub_tree = build_tree(file_path, depth + 1)
            if sub_tree:
                tree += "|   " * depth
                tree += f"+-- {file}\n"
                tree += sub_tree
                has_relevant_files = True
        else:
            ext = os.path.splitext(file)[-1].lower()
            if ext not in ['.py', '.json', '.txt']:
                continue
            tree += "|   " * depth
            tree += f"|-- {file}\n"
            has_relevant_files = True
    if not has_relevant_files:
        return ""
    return tree


directory_path = os.getcwd()
tree = build_tree(directory_path)
with open('tree.txt', 'w') as f:
    f.write(tree)
print("Project tree written to tree.txt")
