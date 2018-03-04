mango
=====

fire up the dev environment:
```bash
echo MANGO_MODE=dev > .env
docker-compose up --build 
```

just the backend:
```bash
cd backend/
# create & activate venv
pip install -r backend/requirements.txt
pip install --editable .
MANGO_MODE=dev mangoctl run
```

just the frontend:
```bash
cd frontend/
yarn start
# for tests
yarn test
```

explore the cli
```bash
mangoctl --help
```
