#!/bin/sh                                                                                                         
tmux new-session -d ncmpcpp
tmux split-window -h ncmpcpp -s visualizer
tmux split-window -v ncmpcpp -s clock
tmux split-window -h alsamixer
tmux -2 attach-session -d
