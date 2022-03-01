import chevron


def create_output_file(data):
    output = ""
    with open('index.ms', 'r') as f:
        output = chevron.render(f, data)

    with open('..\\output\\index.html', 'w', encoding='utf8') as f:
        f.write(output)


if __name__ == '__main__':
    data = {
        "title": "The incredible hulk",
        "description": "Who will win, who will lose?",
        "characters": [
            {'name': 'hulk0', 'url': 'http://i.annihil.us/u/prod/marvel/i/mg/5/a0/538615ca33ab0/portrait_xlarge.jpg'},
            {'name': 'hulk2', 'url': 'http://i.annihil.us/u/prod/marvel/i/mg/3/70/5269581a55d0c/portrait_xlarge.jpg'},
            {'name': 'hulk3', 'url': 'http://i.annihil.us/u/prod/marvel/i/mg/2/e0/5274112b036ff/portrait_xlarge.jpg'},
            {'name': 'hulk4', 'url': 'http://i.annihil.us/u/prod/marvel/i/mg/7/20/527bb5d64599e/portrait_xlarge.jpg'},
            {'name': 'hulk5', 'url': 'http://i.annihil.us/u/prod/marvel/i/mg/9/20/4ce18a92c7a50/portrait_xlarge.jpg'}
        ],
        "attributiontext": "Data provided by Marvel. © 2022 MARVEL"
    }
    create_output_file(data)