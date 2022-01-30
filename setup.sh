#!/bin/bash

sudo pip3 install bs4 \
  requests \
  datetime

echo '{
    "username": "_username",
    "password": "_password"
}' > credentials.json