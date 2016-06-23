#!/bin/bash

set -e
set -x

# This is necessary because /vagrant may not be mounted when uwsgi initially
# starts. The result of that is that uwsgi fails. By the time this runs,
# /vagrant will definitely be mounted.

service uwsgi restart
