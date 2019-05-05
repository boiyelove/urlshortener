import requests
from bs4 import BeautifulSoup

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Crawler(object):
	def __init__(self, url):
		self.r = requests.get(url)
		self.html_context = self.r.text
		self.soup = BeautifulSoup(self.html_context, 'lxml')


	def get_title(self):
		return self.soup.title.String

	def get_description(self):
		# First get the meta description tag
		description = self.soup.find('meta', attrs={'name':'og:description'}) or self.soup.find('meta', attrs={'property':'description'}) or self.soup.find('meta', attrs={'name':'description'})

		# If description meta tag was found, then get the content attribute and save it to db entry
		if description:
		   return description.get('content')
		return None