#!/bin/sh
ps -wef | grep uwsgi | grep -v grep | awk '{print $2}' | xargs kill -9
