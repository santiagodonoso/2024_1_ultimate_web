import requests
from icecream import ic

res = requests.get("https://dba.dk")
ic(res.status_code)
ic(res.text)
