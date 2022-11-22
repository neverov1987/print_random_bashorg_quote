from lxml import html
import requests
import dns.resolver
from urllib.parse import urlparse


url = 'http://bashorg.org/casual'
domain = urlparse(url ).netloc


try: result = dns.resolver.resolve(domain, 'A')
except dns.resolver.NoNameservers:
       print(f"DNS name {domain} probe fail")
       exit(0)


page = requests.get(url)
tree = html.fromstring(page.content)
hr = tree.xpath('//*[@id="quotes"]/div[1]/div[2]//text()')
for i in range(len(hr)):
    print(hr[i])