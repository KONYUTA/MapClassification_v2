#!/bin/zsh

mkdir converted/image
echo "./image/ファイル内の全jpeg画像をpngに変換します。時間がかかるのでその間に草餅でもどうぞ。"
i=0
n=$(ls -l ./image|wc -l)
find image | while read png;do
	convert ${png} -quality 100 converted/${png}.jpg
	printf "\r%s / %s files converted." ${i} ${n}
	i=$((${i}+1))
done
printf "\rall files converted(´・ω・)"
