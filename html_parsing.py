# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
fake_html_1 = '<a href="google.com"> Google! </a> arrrrgghjjjj'
fake_html_2 =  '<a href="google.com"> <a href="ayy"> ayy</a> </a> arrrrgghjjjj'


#takes in html code beginning with '<' and outputs the tag including the <></>
def get_tag_content(html):
    start_tag = html[:html.find(' ')]
    end_tag = '</' + html[1:html.find(' ')] + '>'
    
    print(start_tag)
    print(end_tag)
    
    inner_tags=0
    c=1
    while ( html[c:].find(start_tag) < html[c:].find(end_tag) ) and (html[c:].find(start_tag) != -1):
        inner_tags += 1
        c += html[c:].find(start_tag) + 1
     
    print(inner_tags) 
    while inner_tags > 0:
        c += html[c:].find(end_tag) + 1 
        inner_tags -= 1
        
    return html[:c+html[c:].find(end_tag)+len(end_tag)]    
    
    
#like get_tag_content() but without <></>    
def get_inner_tag_content(html):
    html = get_tag_content(html)
    return html[html.find('>')+1:html.rfind('<')-1]
    
    
def get_tag_attributes(html):
    c = 0
    ret = {}
    html = html[html.find(' '):html.find('>')].strip(' ><')
    print html
            
        
        
        
        
        
        
        
        