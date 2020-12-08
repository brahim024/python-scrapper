from urllib.request import urlopen
try:
	html=urlopen('https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests')
except HTTPError as e:
	print(e)
else:
	print("not found")