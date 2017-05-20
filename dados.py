#!/usr/local/bin/python
import urllib2,cookielib
import html

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

#url = "http://www1.tce.rs.gov.br/aplicprod/f?p=50500:10:::NO:10:P10_ID_LICITACAO,P10_PAG_RETORNO,F50500_CD_ORGAO:499300,14,45000&cs=1JSXuUagjM_8kAM84IkEH6Zk3Zvc"
url ="http://www1.tce.rs.gov.br/aplicprod/f?p=50500:10:::NO:10:P10_ID_LICITACAO,P10_PAG_RETORNO,F50500_CD_ORGAO:481041,14,45000&cs=1OZh64oSBzY5NleMGwz35aIW1tSU"
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(url, headers=headers)

try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

content = page.read()
print content