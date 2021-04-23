# [Bachelor's of Software Development Capstone Project](https://developernexus.herokuapp.com/)

## Project Overview

This project is the culmination of my degree program and includes full lifecycle development.  The documentation covers requirements analysis, design, implementation, testing and delivery.  As software development is evolving, I choose [Django](https://www.djangoproject.com/) as my framework - a popular solution that I had not worked with before.  Django is built with [Python](https://www.python.org/) as well as including [a template language](https://docs.djangoproject.com/en/dev/ref/templates/language/) and an [ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) which allows creating [models](https://docs.djangoproject.com/en/dev/topics/db/models/) of data and letting Django deal with all aspects of the backend database.  [SQLite](https://www.sqlite.org/) was used as the development database and [PostgreSQL](https://www.postgresql.org/) is used in production.  [The Bootstrap Framework](https://getbootstrap.com/) is used to augment the frontend.

<br>

## Project Requirements

Perform a full lifecycle development of a software system, including requirements analysis, designing, implementing, testing and delivery.  Project must include the following elements:

* Data - offline data storage (PostgreSQL is used)
* Verification and Validation - user input is verified and validated
* Re-usable Code - multiple examples of code re-use
* In-code Documentation - sufficiently explains code intent/workings

### Notes

* This project was created and tested on Windows 10 64bit using Python v3.8.7/32-bit and the embedded SQLite3 database v.3.33.0
* This project was deployed and tested on Heroku using Python v3.6.13/64-bit with a managed PostgreSQL database, v13.2

### Dependencies

* Top-level Python libraries used as documented in requirements.txt:

**Package** | **Version**
------------|------------
cryptography | 3.4.6
dj-database-url | 0.5.0
dj-email-url | 1.0.2
Django | 3.1.7
django-allauth | 0.44.0
django-cache-url | 3.2.3
django-coverage-plugin | 1.8.0
django-crispy-forms | 1.11.1
django-debug-toolbar | 3.2
django-extensions | 3.1.2
environs | 9.3.1
gunicorn | 20.0.4
pipdeptree | 2.0.0
psycopg2-binary | 2.8.6
ptpython | 3.0.17
werkzeug | 1.0.1
wheel | 0.36.2
whitenoise | 5.2.0

<br>

## Installation and Setup

### Local

* Install [Python](https://www.python.org/downloads/)
  * Note: Python v3.6 or later required
* Install packages:  pip install -r requirements.txt
* Clone [this repo](https://github.com/sockduct/dusseldorf)
* ...
  * ...

  ```python
  command1
  command2
  ...
  ```

### Heroku

* ...

<br>

## Project Layout

* app1 - description
  * module1 - description
* ...

<br>

## Example Screenshot/Animated GIF

...

<br>

## Resource Attribution

* The following resources were used in coming up with the solution for this project:
  * Django books

<br>

## Project Documents

* [README (What you're reading!)](README.md)
* [Review Instructions](Review.md)
* [Write-up](Write-up.md) - Project write up per requirements above

<br>

## License

[MIT License](LICENSE)
