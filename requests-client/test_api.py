#!/usr/bin/env python

import requests

def probe_api(url):
    r = requests.get(url)
    if r.status_code == 200:
        result = r.json()
        print "%s: %s" % (r.url, result)
        if type(result) is list:
            for x in result:
                if r.url[-1:] != '/' and x[0] != '/':
                    sep = '/'
                else:
                    sep = ''
                probe_api(r.url + sep + x)
        else:
            for x in result:
                print "    %s: %s" % (x, result[x])
    else:
        print "%s: %d" % (r.url, r.status_code)

#url = 'http://localhost:8080/api'
url = 'http://localhost:5000'

print("Verify that the server is at %s" % url)
probe_api(url)
