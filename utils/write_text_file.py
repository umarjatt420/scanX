
def write_text_lines(file_path, text_lines):
    """writing text line in file."""
    with open(file_path, 'w') as f:
        for line in text_lines:
            line += '\n'
            f.write(line)