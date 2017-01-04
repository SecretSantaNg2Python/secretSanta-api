API in Flask

The database is using SQLite.

## setup for api consumption
1. if not `virtualenv --version`, then `pip install virtualenv`, may need `sudo` on that.
2. `virtualenv env`
3. `source env/bin/activate`
4. `pip install -r requirements.txt`
5. `python app.py`

To close the virtual environment, run `deactivate`

To start up again, if no changes have been made on the api, run steps 3 and 5 again.

To make changes on api, like if modules were added:
1. you should already be in the virtual env
2. install any new packages
To download the dependencies, run `pip install -r requirements.txt`

To start the app, run `python app.py`
