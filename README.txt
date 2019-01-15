## Installation

```

pip install Flask
python app.python```


## Description

## Implementation

This project is implemented using Flask, and is a REST API for a store.

## IN APP.PY FILE, CHANGE THE USER NAME TO YOUR USER NAME, I.E.:

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://Tyler:postgres@localhost/gather_python')

    TO 

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://YOUR_USER_NAME:postgres@localhost/gather_python')