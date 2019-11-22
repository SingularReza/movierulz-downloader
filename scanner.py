import requests
import urllib.request
from bs4 import BeautifulSoup

def magnet_link(movie_url, movie_name):
	print(movie_url)
	response = requests.get(movie_url)

	soup = BeautifulSoup(response.text, "html.parser")

	# getting the magnet link from the anchor tag
	link_object = soup.find('a', {'class': 'mv_button_css'})
	magnet_link = link_object.get('href')

	print("Magnet link found for movie {0}: link - {1} \n ".format(movie_name, magnet_link))

	return magnet_link


def scanner(url):
	response = requests.get(url)

	soup = BeautifulSoup(response.text, "html.parser")

	# thread_name used to create folder for storing the corresponding images
	movies = soup.findAll('div', {'class': 'cont_display'})

	#prints total number of images to be downloaded
	print("No of movies found: ", len(movies)-2)

	for index, movie in enumerate(movies):
		# gets movie name and link from the anchor tag
		movie_object = movie.find('a')
		movie_link = movie_object.get('href')
		movie_name = movie_object.get('title')

		if index > 2:
			print("Movie {0}: {1}, link: {2} \n".format(index-1, movie_name, movie_link));
			download_torrent(magnet_link(movie_link, movie_name), movie_name)

def download_torrent(magnet, movie_name):
	response = requests.post("http://localhost:8081/command/download", {'urls': magnet})
	print("Downloading movie: {0} with response {1} \n".format(movie_name, response))

def filterQuality():
	print("nothing")

if __name__ == '__main__':

	# takes the url for the thread you wanted to download the images from
	# make sure that the url has the protocol thingy as the prefix
	url = input("Enter the url for the page: ")
	scanner(url)

 