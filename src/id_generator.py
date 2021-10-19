import json
import random


ids = [1, 2, 3]


def return_id(object):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    upper_chars = chars.upper()

    id = "".join([random.choice([(random.choice(random.choice([chars, upper_chars]))),
                                 str(random.randint(0, 9))]) for _ in range(7)])
    id = object + '-' + id

    try:
        ids.index(id)
        return return_id(object)
    except ValueError:
        ids.append(id)
        with open('src/ids.json', 'w') as f:
            json.dump(ids, f, indent=2)

        return id
