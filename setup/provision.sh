#!/bin/bash

set -e
set -x

apt-get update
apt-get -y upgrade
apt-get -y install python3-pip nginx uwsgi uwsgi-plugin-python3

pip3 install -r /vagrant/setup/requirements.txt

sudo -u www-data sqlite3 /vagrant/pancake.db < /vagrant/setup/schema.sql
sudo -u www-data sqlite3 /vagrant/pancake.db < /vagrant/setup/initial_data.sql

cp /vagrant/setup/nginx.conf /etc/nginx/sites-available/app.conf
ln -fs /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf
rm -f /etc/nginx/sites-enabled/default

cp /vagrant/setup/uwsgi.ini /etc/uwsgi/apps-available/app.ini
ln -fs /etc/uwsgi/apps-available/app.ini /etc/uwsgi/apps-enabled/app.ini

service uwsgi restart
service nginx restart
