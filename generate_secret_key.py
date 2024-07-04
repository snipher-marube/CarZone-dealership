import os
from decouple import config
from django.core.management.utils import get_random_secret_key

env_file = '.env'

# Check if .env file exists and contains SECRET_KEY
if not os.path.exists(env_file) or 'SECRET_KEY' not in open(env_file).read():
    secret_key = get_random_secret_key()
    with open(env_file, 'a') as f:
        f.write(f'\nSECRET_KEY={secret_key}\n')
    print(f'SECRET_KEY generated and written to {env_file}')
else:
    print(f'{env_file} already exists with SECRET_KEY. SECRET_KEY generation skipped.')