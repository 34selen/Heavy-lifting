#!/bin/bash

NAME_CHALL="heavy_lift"

MAPPORT=$1

docker compose -p "ctf-${NAME_CHALL}-${MAPPORT}" down