#!/bin/bash

mkdir -p ../models
python CNNLSTM.py 1> ../models/console.logs 2> ../models/console.logs
