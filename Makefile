.PHONY: setup
setup: install-deps
	@python manage.py syncdb
	@python manage.py migrate
	@python manage.py createsuperuser

install-deps:
	@pip install -r requirements.txt

migrate:
	@python manage.py migrate

create_admin:
	@python manage.py createsuperuser

.PHONY: statics
statics:
	@python manage.py collectstatic --noinput

.PHONY: deploy
deploy:
	@git push heroku master

run:
	@python manage.py runserver 0.0.0.0:8000

tests:
	@python manage.py test