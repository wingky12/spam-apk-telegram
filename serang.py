import requests

pesan ="tobat bang bulan puasa nih"
url = "https://api.telegram.org/bot6472905395:AAHS75eTcM_ZYqjU-uSHSsH0hpWhqWCINZc/sendMessage?parse_mode=markdown&chat_id=6794630646&text='puasa bro?'"

i = range(int(input("masukkan jumlah spam:")))

for n in (i):
	print("kirim spam ke pelaku ",n)
	print("teks yang dikirim" + pesan) 
	x  = requests.get(url)
	print(x.json())




