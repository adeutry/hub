import urllib.request as url
import sys

site = 'http://reddit.com/'

if sys.argv[1]== 'hot':
	site = "http://reddit.com/hot/"
if sys.argv[1]== 'top':	
	site = "http://reddit.com/top/"
	
response = url.urlopen(site)
html = str(response.read())

print('<div class="reddit_column">')

if sys.argv[1] == 'hot':
	print('<div id="reddit_column_info">reddit trending</div>')
if sys.argv[1] == 'top':
	print('<div id="reddit_column_info">reddit top</div>')
#counter 
i = 1
c = 0
e = 0

#get post score
score_start = c + html[c:].find('<div class="score unvoted">')+27 
score_end = score_start + html[score_start:].find('</div>')
score = html[score_start:score_end]
c = html.find('<a class="title may-blank "')

while (c!=-1):
	ret = '<div id="reddit_div_' + str(i) +'" class="reddit_div '
	if i%2==0:
		ret+= 'even'
	ret+= '"><a href='
	c = e + c
	
	
	
	url_start = c + html[c:].find('href="') + 6
	url_end   = url_start + html[url_start:].find('"')
	
	#handle internal links
	if html[url_start:url_start+3]=="/r/":
		ret+= "http://www.reddit.com"
	ret+= html[url_start:url_end] + '>'
	s = url_end + html[url_end:].find('>') + 1
	e = s + html[s:].find('</a>')
	ret+= html[s:e] + '</a>'
	
	#insert score div
	ret+='<div id="score_' + str(i)+'" class="score">' + score + '</div>'
	
	ret+='</div>' #close div
	print(ret)
	
	#get post score
	score_start = c + html[c:].find('<div class="score unvoted">')+27 
	score_end = score_start + html[score_start:].find('</div>')
	score = html[score_start:score_end]
	
	c =  html[e:].find('<a class="title may-blank "')
	i+=1
	
print('</div>')	