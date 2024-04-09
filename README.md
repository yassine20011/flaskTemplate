# Flask template

## Description

This Flask app template offers a robust foundation for your project. With TailwindCSS, you get flexible styling, and the project's tree structure is adaptable to any Flask project. Whether you're a beginner or a seasoned developer, this template simplifies your workflow, making it an ideal choice for any project.


## Features

- **Flask**: A micro web framework written in Python.
- **TailwindCSS**: A utility-first CSS framework for rapid UI development.

## Project structure

```bash
.
├── app.py
├── config.py
├── package.json
├── package-lock.json
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   ├── input.css
│   │   └── output.css
│   ├── images
│   │   ├── flask.svg
│   │   └── tailwindcss.svg
│   └── js
├── tailwind.config.js
├── templates
│   └── index.html
└── views
    └── root.py

7 directories, 13 files
```

- **app.py**: The main file that runs the Flask app.
- **config.py**: Contains the configuration settings for the app such as the database URI,different environments, and the secret key.
- **package.json** and **package-lock.json**: Contains the dependencies for the project.
- **requirements.txt**: Contains the Python dependencies for the project.
- **static**: Contains the CSS, images, and JavaScript files.
- **tailwind.config.js**: Contains the configuration settings for TailwindCSS.
- **templates**: Contains the HTML files.
- **views**: Contains the Python files that handle the routes.

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python3 app.py
```

Create a .env file in the root directory and add the following:

```bash
FLASK_ENV='development' # the app by default runs in development mode
SECRET_KEY='your_secret_key'
DEVELOPMENT_DATABASE_URI=sqlite:///development_sqlite3.db
TESTING_DATABASE_URI=sqlite:///testing_sqlite3.db
PRODUCTION_DATABASE_URI=sqlite:///your_production_database.db
```

You can generate a secret key using the following command:

```bash
python3 -c 'import os; print(os.urandom(16).hex())'
```

To watch the changes in your CSS file, run the following command:

```bash
npm run watch
```