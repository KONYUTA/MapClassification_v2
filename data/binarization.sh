#!/bin/zsh
find image | while read png;do
	convert -threshold 90% ${png} converted/${png}
done
