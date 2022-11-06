#!/bin/zsh
cd DBServer
zsh run_silent.sh &
cd ../APServer
zsh run.sh &
cd ../
