# Gather Cafe - Backend API

Hello and welcome to Gather Cafe! This is the backend repository for a RESTful API intended to order food and beverages. It will display menus, generate orders, process payments, and place the orders with Gather Cafe. Cafe staff will then notify the user when the order has been processed and completed.

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
    -twilio~=6.0.0

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

## Running the tests

User creation in PostMan
<img src ="https://s3.amazonaws.com/gather-screenshots/PM_create_user.png" alt="create user" height=400px width=600px />

User authentication in PostMan
<img src ="https://s3.amazonaws.com/gather-screenshots/PM_auth_user.png" alt="generate token" height=400px width=600px />

Successful get request in PostMan
<img src ="https://s3.amazonaws.com/gather-screenshots/PM_get.png" alt="Get" height=400px width=600px />

Successful deployment to Netlify
<img src ="https://s3.amazonaws.com/gather-screenshots/netlify_overview.png" alt="get" height=400px width=600px />

Interfacing with Stripe for payment authorization
<img src ="https://s3.amazonaws.com/gather-screenshots/stripe_auth.png" alt="conf" height=400px width=600px />

Successful Stripe tests
<img src ="https://s3.amazonaws.com/gather-screenshots/stripe_acct.png" alt="conf" height=400px width=600px />

<!-- ### And coding style tests

Explain what these tests test and why

```
Give an example
``` -->
<!--
## Deployment

Add additional notes about how to deploy this on a live system -->

## Built With

(\*) = New tech learned during development

- [Python](https://www.python.org/) - The programming language used(\*)
- [Flask](http://flask.pocoo.org/) - Python microframework(\*)
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit(\*)
- [PostgreSQL](https://www.postgresql.org/)-Database
- [Netlify](https://www.netlify.com/) - Server(\*)
- [Stripe](https://stripe.com/) - Online payment processing(\*)
- [Twilio](https://www.twilio.com/) - Communications API(\*)

<!-- ## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). -->

## Author

- **Tyler Pritchard** - _Initial work_ - [website](https://tylerrobertpritchard.com)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details -->

## Acknowledgments

- Mansoor Baharamand, Lead Instructor
- Carl Corsini, Assistant Instructor
- Jack Chi, Consultant
- Evin Sellin, Consultant
