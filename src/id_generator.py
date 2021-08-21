import json
import random

with open('src/ids.json', 'r') as f:
    ids = json.loads(f.read())

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


print(return_id('grass_block'))
