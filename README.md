mango
=====

fire up the dev environment:
```bash
echo MANGO_MODE=dev > .env
docker-compose up --build 
```

just the backend:
```bash
# create & activate venv
pip install -r backend/requirements.txt
MANGO_MODE=dev python backend/run.py
```
