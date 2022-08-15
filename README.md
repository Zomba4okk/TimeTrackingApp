## Initial requirements
![image](https://user-images.githubusercontent.com/49648818/184544936-e7d719e3-be51-4d86-81d8-e3386622a099.png)
## DB Schema
![DB schema](https://user-images.githubusercontent.com/49648818/184548398-75c99aec-7024-4bfa-a088-ec95765cd82b.jpg)
## Setup project
- **User python3.8 or higher**
- install dependencies: `pip install -r requirements.txt`
- setup pre-commit hooks: `pre-commit install`
- run migrations: `python manage.py migrate`
- run tests: `python manage.py test`
- generate data for local development: `python manage.py generate_data`
- run server: `python manage.py runserver`
## Useful info
Check `<host>/docs` URL for swagger documentation.
