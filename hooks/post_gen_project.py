"""
This module is executed before the cookiecutter creation.
"""
import os
import json
import string
import random

PATH = os.getcwd()
IDENTITY_PATH = os.path.join('.identity.json')

with open(IDENTITY_PATH, mode='r') as file:
    identity_dict = json.load(file)


# Now we need to actually perform the anonymization, which means that we will go through every file in the
# repository and replace all the non-anonymous string versions with the anonymous hashes
if '{{ cookiecutter.anonymize }}' == 'y':

    for root, folders, files in os.walk(PATH):
        for file_name in files:
            # We need to make sure that we DO NOT apply this on the identity file itself, because then we
            # would overwrite all the real strings in there as well and completely loose any reference
            # to the real information
            if file_name == '.identity.json':
                continue

            file_path = os.path.join(root, file_name)
            with open(file_path, mode='r') as file:
                content = file.read()

                for identity_key, identity_data in identity_dict.items():
                    content = content.replace(identity_data['real'], identity_data['anon'])

            with open(file_path, mode='w') as file:
                file.write(content)
