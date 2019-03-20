# Flask Backend Implementation

## How to run
### 1. Config a venv for the backend (with python -v >= 3.6)
### 2. install packages
```
$ pip install -r requirements.txt
```
### 3. set env variables for auth.py
### 4. run in debug mode
```
$ python3 run.py
```
### 5. run in production mode
```
$ gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## How to Deploy
After fully test all the implementation you have done in this brunch, please create a `pull request` to branch `production`. Once the pull request has been committed, your changes will be automatically deployed to http://gobo-api.cfapps.io
