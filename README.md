# Project Title

Hello and welcome to Gather Cafe! This application is intended to order food and beverages specifically from the Gather Cafe located in the Galvanize building at 44 Tehama St in San Francisco, CA. It will display menus, generate orders and place the orders with Gather Cafe. Gather staff will then notify the user when the order has been processed and completed.

## Getting Started

IN APP.PY FILE, CHANGE THE USER NAME TO YOUR USER NAME, I.E.:

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
'DATABASE_URL', 'postgresql://Tyler:postgres@localhost/gather_python')

    TO

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
'DATABASE_URL', 'postgresql://YOUR_USER_NAME:postgres@localhost/gather_python')

### Prerequisites

You'll need to install:

    -Python (Minimum )
    -Flask
    -Flask-JWT
    -Flask-RESTful
    -Flask-SQLAlchemy
    -flask-cors
    -uwsgi
    -psycopg2
    -bcrypt

### Installing

```
pip install Flask
```

```
pip install stripe
```

```
python app.python from the command line in the folder's root directory
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

<img src ="https://s3.amazonaws.com/gather-screenshots/PM_auth_user.png" alt="auth" height=800px width=800px />

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

- [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
- [Maven](https://maven.apache.org/) - Dependency Management
- [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

- **Billie Thompson** - _Initial work_ - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Mansoor Baharamand, Lead Instructor
- Carl Corsini, Assistant Instructor
- Jack Chi, Consultant
- Evin Sellin, Consultant
