# Flask Backend Implementation

## How to run
### 0. Note, workdir is `backend/`, make sure you are under the correct directory
$ cd backend
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
### 6. About credentials
Getting rid of hard-coded service credentials can be time consuming in the moment. Considering it's a private school project, we'll just do the hard-coded way for now, but definitely should and will avoid that in future updates, for privacy and security considerations.
## How to Deploy
After fully test all the implementation you have done in this brunch, please create a `pull request` to branch `production`. Once the pull request has been committed, your changes will be automatically deployed to http://gobo-api.cfapps.io