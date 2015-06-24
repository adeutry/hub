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

#get post comments
comment_url_start = c + html[c:].find('<li class="first"><a href="') +27
comment_url_end   = comment_url_start + html[comment_url_start:].find('"')
comment_url       = html[comment_url_start:comment_url_end]
        
    #get post comment value
if html[comment_url_end:].find('class="comments empty may-blank"') > html[comment_url_end:].find('class="comments may-blank"'):
    comment_value_start = comment_url_end + html[comment_url_end:].find('class="comments may-blank" >') +28
    comment_value_end   = comment_value_start + html[comment_value_start:].find('comment')-1
    comment_value       = html[comment_value_start:comment_value_end]
else:
    comment_value = '-'
         




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
		
	#insert title link	
    ret+= html[url_start:url_end] + '>'
    s = url_end + html[url_end:].find('>') + 1
    e = s + html[s:].find('</a>')
    ret+= html[s:e] + '</a>'
    
	#commet and score div
    ret+='<div class="score_comments">'
    #insert score div
    ret+='<div id="score_' + str(i)+'" class="score">' + score + '</div>'
        
    #insert comment div
    ret+='<div id="comment_'+ str(i) +'" class="comment"><a id="comment_link_' + str(i) +'" href="' + comment_url +'">' + comment_value + '</a></div>'
    
    ret+='</div></div>' #close div
    print(ret)
	
    
    #get post score
    score_start = c + html[c:].find('<div class="score unvoted">')+27 
    score_end = score_start + html[score_start:].find('</div>')
    score = html[score_start:score_end]

    c =  html[e:].find('<a class="title may-blank "')
    m= e + c
    #get post comments
    comment_url_start = m + html[m:].find('<li class="first"><a href="')+27
    comment_url_end   = comment_url_start + html[comment_url_start:].find('"')
    comment_url       = html[comment_url_start:comment_url_end]
     
    #get post comment value
    if (html[comment_url_end:].find('class="comments empty may-blank"') > html[comment_url_end:].find('class="comments may-blank"')) or (html[comment_url_end:].find('class="comments empty may-blank"') == -1):
        comment_value_start = comment_url_end + html[comment_url_end:].find('class="comments may-blank" >') +28
        comment_value_end   = comment_value_start + html[comment_value_start:].find('comment')-1
        comment_value       = html[comment_value_start:comment_value_end]
    else:
        comment_value = '-'
        

   
    i+=1
    
print('</div>')    
