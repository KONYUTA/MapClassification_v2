#!/bin/zsh
ps |grep run.sh|awk '{print $1}'|while read num;do
	kill ${num} > /dev/null 2>&1
done
ps |grep spring|awk '{print $1}'|while read num;do
	kill ${num} > /dev/null 2>&1
done
ps |grep mbtile|awk '{print $1}'|while read num;do
	kill ${num} > /dev/null 2>&1
done
echo '\n\n\nサーバーが終了しましたよ(´･ω･`)\n'
