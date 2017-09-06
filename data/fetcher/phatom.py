"""phatom.py"""

from .base import Fetcher
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PhatomJSFetcher(Fetcher):

    """PhatomJS based fetching"""

    def __init__(self, *args, **kwargs):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 ",
        "(KHTML, like Gecko) Chrome/15.0.87")
        self.desired_capabilities = kwargs.get("desired_capabilities", dcap)
        super(PhatomJSFetcher, self).__init__(*args, **kwargs)
    
    def on_fetch(self, url, loop=None, **extra):
        """on fetch callback for phatomjs"""
        driver = webdriver.PhantomJS(desired_capabilities=self.desired_capabilities)
        driver.get(url, **extra)
        return driver.page_source