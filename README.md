# Example Master Controller + Processing Controller


## Quickstart

Set up a virtualenv:

```bash
pip3 install -U virtualenv
pip3 install -U autoenv
````


```
virtualenv -p python3 venv
```




```bash
export FLASK_APP=mc-service/app.py
export FLASK_DEBUG=True
flask initdb
flask run
```
