import requests
import urllib.request
from bs4 import BeautifulSoup

def scanner(url):
	response = requests.get(url)

	soup = BeautifulSoup(response.text, "html.parser")

	# thread_name used to create folder for storing the corresponding images
	torrent_list = soup.findAll('li')

	for index, torrent in enumerate(torrent_list):
		# gets movie name and link from the anchor tag
		torrent_object = torrent.find('a')
		torrent_link = torrent_object.get('href')

		if index > 2:
			download_torrent(torrent_link)

def download_torrent(magnet):
	print('https://catbox.moe/'+magnet)
	file = open("file.txt", "a")
	file.write('https://catbox.moe/'+magnet+'\n')


if __name__ == '__main__':

	# takes the url for the thread you wanted to download the images from
	# make sure that the url has the protocol thingy as the prefix
	url = input("Enter the url for the page: ")
	scanner(url)

 