#!/usr/local/bin/python
# coding: utf8

import re
import HTMLParser
import urllib2,cookielib

parser = HTMLParser.HTMLParser()


url_base ="http://www1.tce.rs.gov.br/aplicprod/{0}"
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

with open('dados.html') as fp:
    dados = ""
    tr=False
    print ('Valor Homologado/Contratado\tModalidade\tNúmero\tAno\tValor Estimado\tData Abertura\tSituação')
    for line in fp:
        if re.match('([^\<]*)(\<tr\>)(.*)', line):
            if len(dados) > 0:
                print dados.encode('utf-8')
                dados = ""
            tr=True
        elif re.match('(.*)(a-IRR-header)(.*)', line):
            continue
        elif tr and re.match('([^\<]*)(\</tr\>)(.*)', line):
            tr=False
        elif tr and re.match('(.*)(headers=\"LINK\")(.*)', line):
            m = re.search('(.*)(\<td headers=\"LINK\"><a href=\")([^\"]+)(.*)', line)
            url = url_base.format(parser.unescape(m.group(3)))
            req = urllib2.Request(url, headers=headers)
            content = ""
            try:
                page = urllib2.urlopen(req)
                content = page.read()
            except urllib2.HTTPError, e:
                content=""
            valor = ''
            if len(content) > 0:
                content_arr = content.split()
                for i, l in enumerate(content_arr):
                    if 'Homologado' in l:
                        valor = content_arr[i + 4]
                        break
                if len(valor) == 0:
                    for i, l in enumerate(content_arr):
                        if '#LBL_VL_ESTIMADO#' in l:
                            valor = content_arr[i + 4]
                            break
                valor = valor.strip()
            dados += "0,00\t" if valor[0] == '-' else valor.replace('.', '') + '\t'
        elif tr and re.match('(.*)(C12863026905211221)(.*)', line):
            m = re.search('(.*)(C12863026905211221\">)(.+)(<)(.*)', line)
            dados += parser.unescape(m.group(3)) + '\t'
        elif tr and re.match('(.*)(C12861081312211213)(.*)', line):
            m = re.search('(.*)(C12861081312211213\">)(.+)(<)(.*)', line)
            dados += parser.unescape(m.group(3)) + '\t'
        elif tr and re.match('(.*)(C12861498241211214)(.*)', line):
            m = re.search('(.*)(C12861498241211214\">)(.+)(<)(.*)', line)
            dados += parser.unescape(m.group(3)) + '\t'
        # elif tr and re.match('(.*)(C12865836612211236)(.*)', line):
        #     m = re.search('(.*)(C12865836612211236\">)(.+)(<)(.*)', line)
        #     dados += parser.unescape(m.group(3)) + '\t' if m != None else '\t'
        elif tr and re.match('(.*)(C12866230394211241)(.*)', line):
            m = re.search('(.*)(C12866230394211241\">)(.+)(<)(.*)', line)
            valor = m.group(3).replace('.', '') 
            dados += "0,00\t" if valor[0] == '-' else valor.replace('.', '') + '\t'
        elif tr and re.match('(.*)(C12865413588211236)(.*)', line):
            m = re.search('(.*)(C12865413588211236\">)(.+)(<)(.*)', line)
            dados += parser.unescape(m.group(3)) + '\t'
        elif tr and re.match('(.*)(C45481316068427303)(.*)', line):
            m = re.search('(.*)(C45481316068427303\">)(.+)(<)(.*)', line)
            dados += parser.unescape(m.group(3)) + '\t'
