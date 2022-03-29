import requests
from bs4 import BeautifulSoup

url = 'https://www.hktvmall.com/hktv/zh/main/Otoyo/s/H6141002/%E6%99%82%E5%B0%9A%E6%9C%8D%E9%A3%BE/%E5%A5%B3%E5%A3%AB%E6%9C%8D%E9%A3%BE/%E5%85%A7%E8%A1%A3-%E7%9D%A1%E8%A1%A3-%E8%A5%AA%E5%AD%90/%E8%A5%AA%E5%AD%90-%E7%B5%B2%E8%A5%AA/%E6%97%A5%E6%9C%AC%E8%A3%BDSABRINA-ActiFit%E7%BE%8E%E8%85%BF%E7%B5%B2%E8%A5%AA-80D-%E9%BB%91%E8%89%B2-ML-%E6%8A%97%E8%8F%8C%E9%98%B2%E8%87%AD-%E9%98%B2%E9%9D%9C%E9%9B%BB-%E4%BF%9D%E6%BF%95-%E9%98%B2%E5%8B%BE/p/H6141002_S_H107-026-ML'

sess = requests.session()
req = sess.get(url)

print(req.text)