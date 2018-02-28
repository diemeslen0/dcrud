# Django CRUD for testing 
> Simple CRUD using Google Auth. 

![PyPi][python-image]
![PyPi][status-image]
![Dockbit][deploy-image]
![Wercker][build-image]

Possible to create a account using Google Authentication and after that
create and manager users.

## Technologies utilized
* Python 3.6.4
* Django 2.0.2
* PostgreSQL 9.5+

### TODO

- [ ] Administrators of the app should authenticate using a Google account
- [ ] Administrators should be able to create, read, update and delete users
- [ ] Restrict manipulation operations on a user to the administrator who created them 
- [x] Use PostgreSQL as the database backend
- [x] Use Python 3.x
- [ ] Write documentation on how to setup, run and use your implementation


## Installation

Any Operating System:

```sh
docker-compose run web python manage.py makemigrations

docker-compose run web python manage.py migrate

docker-compose up

access http://127.0.0.1:8000
```

## Release History

* 0.0.1
    * Project creation

## Meta

Diemesleno Souza Carvalho – [@diemesleno](https://twitter.com/diemesleno) – diemesleno@gmail.com

Distributed under the ![AUR][gpl-image] license. 

[https://github.com/diemeslen0/dcrud](https://github.com/diemeslen0/)

[python-image]: https://img.shields.io/pypi/pyversions/Django.svg?style=flat-square
[gpl-image]: https://img.shields.io/aur/license/yaourt.svg?style=flat-square
[status-image]: https://img.shields.io/pypi/status/Django.svg?style=flat-square
[build-image]: https://img.shields.io/wercker/ci/wercker/docs.svg
[deploy-image]: https://img.shields.io/dockbit/DockbitStatus/health.svg?token=TvavttxFHJ4qhnKstDxrvBXM&style=flat-square
