import socket
import requests
import requests.packages.urllib3.util.connection as urllib3_connection


class IPTestObject():
    def __init__(self, url):
        self.url = url
        self.test = self.test()

    def test(self):
        def _allowed_gai_family():
            family = socket.AF_INET
            if urllib3_connection.HAS_IPV6:
                family = socket.AF_INET6
            return family

        urllib3_connection.allowed_gai_family = _allowed_gai_family

        try:
            requests.get(self.url)
        except:
            return False
        return True

    def __str__(self):
        return("IPv6 test for %s: %s" %(self.url, self.test))
