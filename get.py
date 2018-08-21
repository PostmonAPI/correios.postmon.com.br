import urllib, json
url = "http://localhost:5000/webservice/buscaEventos/?objetos=AA123456789BR"
response = urllib.urlopen(url)
data = json.loads(response.read())
print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8'))
