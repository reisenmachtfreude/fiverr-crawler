import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import sys, os

# Paths and includes
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
workspace_root = os.path.dirname(project_dir)


class FiverrSpider(CrawlSpider):
	name = 'fiverr'
	allowed_domains = ['fiverr.com']
	start_urls = ['https://www.fiverr.com/categories/data/data-analytics?source=category_tree']

	rules = (
		Rule(LinkExtractor(allow=()), callback='parse_item', follow=True, process_request='processRequest'),
	)


	def parse_item(self, response):
		all_url_output_path = os.path.join(project_dir, 'results', 'all_fiver_urls.txt')
		with open(all_url_output_path, 'a') as f:
			f.write(response.url + '\n')


	def processRequest(self, request, response):
		request.headers['authority'] = 'www.fiverr.com'
		request.headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
		request.headers['accept-language'] = 'en-US,en;q=0.9'
		request.headers['sec-fetch-dest'] = 'document'
		request.headers['sec-fetch-mode'] = 'navigate'
		request.headers['sec-fetch-site'] = 'none'
		request.headers['sec-fetch-user'] = '?1'
		request.headers['sec-gpc'] = '1'
		request.headers['upgrade-insecure-requests'] = '1'
		return request