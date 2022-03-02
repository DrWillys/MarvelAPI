import chevron
import os


def create_output_file(data):
    output = ''
    with open('index.mustache', 'r') as f:
        output = chevron.render(f, data)

    filename = '..\\output\\index.html'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf8') as f:
        f.write(output)
