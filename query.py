from urllib import request, parse

postDict = {}
postDict['appReceiptNum'] = 'YSC1990000456'
data = parse.urlencode(postDict).encode()

url = 'https://egov.uscis.gov/casestatus/mycasestatus.do' 
  
req =  request.Request(url, data=data)
resp = request.urlopen(req).read().decode('utf-8')
start = resp.find('<h1>')
end = resp.find('</p>', start) +4
body = (resp[start:end])
title = body[body.find('<h1>')+4:body.find('</h1>')]

print (title)
