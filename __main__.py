# from ipv6tester import __version__
from .iptestobject import iptestobject
import argparse
import re
import sys


def testFromFile(file):
    try:
        with open(file, 'r') as infile:
            urls = infile.read()
            urls = re.findall(r'https?://[\w\d\-\.]+', urls)
    except OSError:
        print("%s not found" %(file))
        return False

    for url in urls:
        print(runIPv6Test(url))


def runIPv6Test(url):
    _test = iptestobject.IPTestObject(url)
    return(_test)


def main(**args):
    parser = argparse.ArgumentParser(description="Test IPv6 connectivity")
    parser.add_argument("--file", "-f", metavar="files", nargs="+",
                        help="Space-separated list of files of URLs to test")
    parser.add_argument("--url", "-u", metavar="url", nargs="+",
                        help="Space-separated list of URLs to test")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    try:
        for file in args.file:
            testFromFile(file)
    except AttributeError:
        pass
    except TypeError:
        pass

    try:
        for url in args.url:
            print(runIPv6Test(url))
    except AttributeError:
        pass
    except TypeError:
        pass

if __name__ == "__main__":
    main()
