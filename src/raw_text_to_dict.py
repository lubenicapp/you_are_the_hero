import json
import re


class Bloc:
    def __init__(self, chapter):
        self.chapter = chapter
        self.text = ''
        self.options = []

    def update_options(self):
        """
        options looks like "rendez vous au 256"
        so I parse a number following 'au'
        """
        numbers = re.findall(r"au\s*\d+", self.text)
        self.options = [int(x.split()[-1]) for x in numbers]


def extract_blocs_from_file(filename):
    blocs = []
    current_bloc = None
    with open(filename) as file:
        for line in file:
            if line.strip().isdigit():  # if the line contains only a number ie: it is a chapter
                if current_bloc:
                    current_bloc.update_options()
                    blocs.append(current_bloc)

                current_bloc = Bloc(int(line.strip()))
            elif current_bloc:
                current_bloc.text += line

    return blocs


def jsonify_blocs(title, blocs, dest_file):
    d = {'title': title}
    for bloc in blocs:
        d.update({bloc.chapter: {'text': bloc.text, 'options': bloc.options}})
    with open(dest_file, 'w') as cf:
        json.dump(d, cf, indent=4)


def jsonify_text(source_file, dest_file):
    blocs = extract_blocs_from_file(source_file)
    title = extract_title(source_file)
    jsonify_blocs(title, blocs, dest_file)


def extract_title(filename):
    """
        With this book collection, fileame are like:
        'Defis Fantastiques - La nuit des morts-vivants.pdf'
        so the title is between the first '-' and '.'
    """
    try:
        title = filename.split('-')[1]
        title = title.split('.')[0]
    except IndexError:
        return 'title_error'
    return title
