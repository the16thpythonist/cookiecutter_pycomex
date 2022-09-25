"""
This module is executed before the cookiecutter creation.
"""
import os
import json
import string
import random

PATH = os.getcwd()
IDENTITY_PATH = os.path.join('.identity.json')


def generate_anon_hash(size: int = 6, chars: str = string.ascii_lowercase + string.digits):
    return 'anon_' + ''.join(random.choice(chars) for _ in range(size))


# This dict will essentially create a mapping between the real values of certain sensitive information
# and an anonymous hash replacement of those.
identity_dict = {
    'author_name': {
        'real': '{{ cookiecutter.author_name }}',
        'anon': generate_anon_hash()
    },
    'author_email': {
        'real': '{{ cookiecutter.author_email }}',
        'anon': generate_anon_hash()
    },
    'github_url': {
        'real': '{{ cookiecutter.repo_url }}',
        'anon': generate_anon_hash()
    }
}

with open(IDENTITY_PATH, mode='w') as file:
    json.dump(identity_dict, file)

