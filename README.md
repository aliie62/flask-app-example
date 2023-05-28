![Build](https://github.com/aliie62/flask-app-example/actions/workflows/build.yml/badge.svg) ![Coverage](https://github.com/aliie62/flask-app-example/blob/master/coverage.svg)

# Store Inventory API

This is a sample Flask API project with Flask-RESFful, Flask-JWT-Extended, Flask-SQLAlchemy, and Docker. This project also has an Actions buid workflow.

<br>

# Prerequisities

This code eas written with Python 3.11.3. Required libraries can be found in _requirements.txt_ file.

<br>

# Installtion

Download or clone the repository in your machine. In the _Command Prompt_ in Windows or _bash_ in Linux, go to folder that you cloned/copied the code. You may want to run virtual environment before installing the depedencies.
<br><br>
There is a Makefile included in this project to assist you with the project life-cycle. To install all dependcies run `make install` in terminal.<br>To learn all commands included in the make file, run `make help` in the terminal.

<br>

# Configuration

There are five below environment variables needed to be defined:

1. SQLITE_URI: your main project database (SQLite) path
2. FLASK_SECRET_KEY: Random byte string for the flask app
3. PYTHONPATH: includes path of your project
4. REDIS_PORT: Port of Redis server is used to store authentication tokens
5. REDIS_HOST: hostname of Redis server is used to store authentication token

# Usage

In the project directory in the terminal run below command:

```
python.exe inventory/app.py
```

This will run the app on `http://127.0.0.1:8080`

<br>

# Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull request.

<br>

# License

Distributed under the _MIT License_. See `LICENSE` for more information.

<br>

# Changelog

Changelog can be found here: [CHANGELOG](CHANGELOG.md)
