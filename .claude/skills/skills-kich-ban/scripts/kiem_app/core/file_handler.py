class FileHandler:
    def read_file(self, filepath: str) -> str:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def write_file(self, filepath: str, content: str):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
