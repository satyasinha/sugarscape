#!/bin/bash

cd view && npm run build

cd .. && flask run

