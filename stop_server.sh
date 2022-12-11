#!/bin/zsh
ps ax |grep run.sh|awk '{print $1}'|while read num;do
	kill ${num} 2> /dev/null
done
ps ax |grep spring|awk '{print $1}'|while read num;do
	kill ${num} 2> /dev/null
done
ps ax |grep mbtile|awk '{print $1}'|while read num;do
	kill ${num} 2> /dev/null
done
echo '\n\n\nサーバーが終了しましたよ(´･ω･`)\n'
