### q1
テスト、入れるだけ

### q2
シーザー暗号、試しにpythonのrot13で複合したらあっさり

### q3
ソースをみるとscriptの中にニャル子さんが。
エラー吐いてないのでjsとして動作するっぽい、まじ？
q3にコピペ
```
node q3 
``` 
おお、でた。

### q5
とりあえずbase64エンコード、
```
echo q4 | nkf -d --base64
```
まだ暗号化されてるっぽい、というかタイトルがonionなるほどと思い数回デコード
```

```
uuencodeっぽい文字列が出現。ビンゴ

### q8
リンクがあるので脳死してクリック、表示がやばい
URLみたらpcapって書いてあったのでlocalに落としてwiresharkで表示した

basic is secure?なんでBasic認証してる通信がありそう→http 401発見
200の直前の通信をみると`Ausentication: XXXXX`
wiresharkが勝手にdecodeしてくれているのでタブを開くとフラグ出現





