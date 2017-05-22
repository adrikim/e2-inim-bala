from sys import argv
script, filename = argv
count = 1
target = open(filename, 'w')
target.truncate()
while (count <= 8):
	from lxml import html
	import requests
	page = requests.get('http://psd.museum.upenn.edu/epsd/epsd/e' + str(count) + '.html')
	tree = html.fromstring(page.content)
	#This will create a list of buyers:
	# buyers = tree.xpath('//div[@class="compounds"]/text()')
	#This will create a list of prices
	#Use this
	word = tree.xpath('//span[@class="cf"]/text()')
	print word
	# summary = tree.xpath('//th[@class="ovyear"]/text()')
	# word.append(tree.xpath('//th[@class="ovyear"]/text()'))
	# prices = tree.xpath('//span[@class="gw"]/text()')
	word.extend(tree.xpath('//span[@class="gw"]/text()'))
	# dates = tree.xpath('//td[@class="ovfreq"]/text()')
	word.extend(tree.xpath('//td[@class="ovfreq"]/text()'))
	word.extend(tree.xpath('//span[@class="w"]/text()'))
	# cuneiform = tree.xpath('//a[@href="javascript:popsign(\'/epsd/psl/img/popup/Obhw.png\',60,109)"]/text()')
	target.write(str(word))
	target.write("\n\n")
	del word[:]
	count = count + 1
target.close()