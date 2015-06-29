# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:13:11 2015

@author: amadeusz
"""
import json
import urllib as url
import MySQLdb 
import time


#array of boards to monitor
boards = ['mu','lit','v','g']

#connect to database
db = MySQLdb.connect(host="localhost", user="root",passwd="password",db="hub", charset="utf8")
cur = db.cursor()

#board is something like 'mu'
def update_4chan_by_board (board):
    site = 'https://a.4cdn.org/' + board + '/catalog.json'
    response = url.urlopen(site)
    html = str(response.read())
    pages = json.loads(html)
    
  
                
    cur.execute("SHOW TABLES LIKE" + "'4chan_" + board +"'")
    if len(cur.fetchall()) == 0:
        cur.execute("CREATE TABLE `4chan_" + board + "` (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,subject TEXT,body TEXT,replies INT UNSIGNED,no INT UNSIGNED) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8" )
    

    i =1
    for page in pages:
        for thread in page['threads']:
            sub = ''
            com = ''
            if 'sub' in thread:
                sub = thread['sub']
            if 'com' in thread:    
                com = thread['com']        
            
            replies = str(thread['replies'])
            no =  str(thread['no'])            
            
            i+=1    
            sql = "INSERT INTO `4chan_" + board + "` (`id`,`subject`,`body`,`replies`,`no`) VALUES ('" + str(i) +"','" + sub +"','" + com + "','" + replies +"','" + no + "') ON DUPLICATE KEY UPDATE subject='" + sub +"', body='" + com + "', subject='" + sub + "', no='" + no + "', replies='" + replies + "'"  
            print(sql + '\n')           
            cur.execute(sql)
         


while True:
    for board in boards:
        update_4chan_by_board(board)
        db.commit()
        time.sleep(5)

        

cur.close()
db.close()         
