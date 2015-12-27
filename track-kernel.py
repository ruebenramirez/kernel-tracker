from lxml import html
import requests
import urllib3.contrib.pyopenssl

# patch up SSL for python
urllib3.contrib.pyopenssl.inject_into_urllib3()

page = requests.get('https://www.kernel.org/')
tree = html.fromstring(page.content)
kernel_html = tree.xpath('//td[@id="latest_link"]/a/text()')
latest_kernel = kernel_html[0]
print(latest_kernel)
