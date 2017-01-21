API in Flask

The database is using SQLite.

## setup for api consumption the first time
1. if not `virtualenv --version`, then `pip install virtualenv`, may need `sudo` on that.
2. `virtualenv env`
3. `source env/bin/activate`
4. `pip install -r requirements.txt`
5. `python app.py`



To close the virtual environment, run `deactivate`

## Start up the server:
1. `source env/bin/activate`
2. `python app.py`

To make changes on api, like if modules were added:

1. you should already be in the virtual env
2. install any new packages
3. `pip freeze > requirements.txt`
4. make the commit and push up to the remote, and remind front-end to run step 4 again.


To drop the database: `rm secretsanta.SQLite`, then start the app again.