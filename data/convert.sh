#!/bin/zsh

mkdir converted/image
i=0
n=$(ls -l ../data/image|wc -l)
find image | while read png;do
	convert -threshold 35% ${png} converted/${png}
	printf "\r%s / %s files converted." ${i} ${n}
	i=$((${i}+1))
done
printf "\rall files converted(´・ω・)"
