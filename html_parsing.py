# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
fake_html_1 = '<a href="google.com"> Google! </a> arrrrgghjjjj'
fake_html_2 =  '<a href="google.com"> <a href="ayy"> <a > ayy</a> </a></a> arrrrgghjjjj'
fake_html_3 = '<a href="google.com" id="some-link" class="something-else"> <a href="ayy"> ayy</a> </a> arrrrgghjjjj'
fake_html_4 = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><title>Lydon</title><link href="main.css" rel="stylesheet" type="text/css" /></head><body><div id="mainDiv"><div id="leftArrow"><a href="page.php?i=13"><img src="images/arrowLeft.bmp" width="100"></img></a></div><div id="centerColumn"><img src="images/banner.bmp" ></img><div id="comicDiv"><img src="images/Transparent Lydon.png" width="300"></img></div><script src="script3.js"></script></body></html>'
fake_html_5 = '<div id="hurr"> asdasd <div class="huee"> sss </div></div>'
fake_html_6 = '<div id="mainDiv"><div id="leftArrow"><a href="page.php?i=13"><img src="images/arrowLeft.bmp" width="100"></a></div><div id="centerColumn"><img src="images/banner.bmp"><div id="comicDiv"><img src="images/Transparent Lydon.png" width="300"></div><script src="script3.js"></script></div></div>'


#takes in html code beginning with '<' and outputs the tag including the <></>
def get_tag_content(html):
    start_tag = html[:html.find(' ')]
    end_tag = '</' + html[1:html.find(' ')] + '>'
    
    print(start_tag)
    print(end_tag)
    
    level=1
    c=1
    while level > 0:
        if (html[c:].find(start_tag) < html[c:].find(end_tag)) and (html[c:].find(start_tag) != -1):
            level += 1
            c += html[c:].find(start_tag)
        else:
            c += html[c:].find(end_tag)
            level -= 1
      
    return html[:c+html[c:].find(end_tag)+len(end_tag)]    
    
    
#like get_tag_content() but without <></>    
def get_inner_tag_content(html):
    html = get_tag_content(html)
    return html[html.find('>')+1:html.rfind('<')-1]
    
#given tag it returns an associative array like attr:value    
def get_tag_attributes(html):
    c = 0
    ret = {}
    html = html[html.find(' '):html.find('>')].strip(' ><')
    print(html)
    while c < len(html):
        attr = html[c:c + html[c:].find('=')]
        val_start = c + html[c:].find('"') + 1
        val_end   = val_start +  html[val_start :].find('"')
        ret[attr] = html[val_start:val_end]
        c = val_end + 2
    return ret    
        
        
def get_tags_by_id(html , id):
    ret=[]
    c = 0
    while c < len(html) and html[c:].find('<') != -1:
        tag_start = c + html[c:].find('<')
        while html[tag_start + 1] == '/' and html[tag_start + 1:].find('<') != -1:
            tag_start = tag_start + 1 + html[tag_start + 1:].find('<')
        attrs = get_tag_attributes(html[tag_start:])    
        if 'id' in attrs:
            if attrs['id'] == id:
                print("inserting")
                ret.append(get_tag_content(html[tag_start:]))
        c = tag_start + 1
    return ret    











        
        
        
