# py-power-checker
kind of power's problem checker for own needs

Installation:

git clone https://github.com/sviiiter/py-power-checker.git

pip install -r requirements.txt

```
git clone https://github.com/sviiiter/py-power-checker.git

pip install -r requirements.txt

./venv/bin/python power_checker.py
```

### OR

docker:

```
docker run -d -v $(pwd):/app -v $(pwd)/docker/cron:/etc/cron.d --entrypoint "/app/docker/entrypoint.sh" sviiiter/ubuntu-cron-python3-pip-jq-curl:v1
```


