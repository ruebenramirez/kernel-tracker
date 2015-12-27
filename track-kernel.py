from lxml import html
import requests
import urllib3.contrib.pyopenssl

import model

# patch up SSL for python
urllib3.contrib.pyopenssl.inject_into_urllib3()


def scrape_current_kernel():
    """
    * scrape latest kernel release version from kernel.org
    * returns string of the current kernel release version
    """
    page = requests.get('https://www.kernel.org/')
    tree = html.fromstring(page.content)
    kernel_html = tree.xpath('//td[@id="latest_link"]/a/text()')
    latest_kernel = kernel_html[0]
    return latest_kernel


def compare_release_versions():
    """
    * is scraped kernel version newer than last one stored?
    """


def send_notification():
    """
    * send notification about new kernel release
    """
    pass


if __name__ == "__main__":
    current_kernel = scrape_current_kernel()
