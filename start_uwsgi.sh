#!/bin/sh
uwsgi -s /var/run/uwsgi/app.sock -d /var/log/facehub/uwsgi.log -M -p 4 --chdir /facehub/app
