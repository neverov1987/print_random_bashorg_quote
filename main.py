from lxml import html
import requests
url = 'http://bashorg.org/casual'

page = requests.get(url)
tree = html.fromstring(page.content)
# hr = tree.xpath('//div[@class="number"]/text()')
hr = tree.xpath('//*[@id="quotes"]/div[1]/div[2]//text()')
# tree.xpath("//div[@class='exchangeRates']/table/tr[5]/td[4]//text()")
for i in range(len(hr)):
    print(hr[i])

