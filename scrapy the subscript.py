#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib3
from bs4 import BeautifulSoup
import re
import json


# In[2]:


url = "https://www.gsb.stanford.edu/business-podcasts/think-fast-talk-smart-podcast"

# 获取TFTS主页
http = urllib3.PoolManager()
r = http.request('GET', url)
print("获取TFTS主页状态：", r.status)

# 解析主页
soup = BeautifulSoup(r.data, 'html.parser')
soup.title.string

# 定位大体位置
target_pos = soup.find('div', class_='views-field views-field-title')

# 解析标题和网址
the_episode_title = str(target_pos.a.string)
the_episode_url = "https://www.gsb.stanford.edu/" + str(target_pos.a["href"])
print("文章标题：", the_episode_title)
print("文章网址：", the_episode_url)


# In[3]:


# 获取文章页面
page = http.request("GET", the_episode_url)
print("获取文章页面状态：", page.status)

# 解析文章页面
page_soup = BeautifulSoup(page.data)

# 定位总体位置
pos = page_soup.find("div", class_='announcement-stories__wrapper-information')


# In[4]:


# 获取标题
title_pos = pos.find('h1', class_='heading has-icon icon-audio-before has-key-taxonomy-above')
title = str(title_pos.string.strip())

# 获取总结
summary_pos = pos.find('p', class_='intro')
summary = str( summary_pos.string.strip() )

# 获取时间和作者列表
infor_pos = pos.find('div', class_='author-info-wrapper')
infor_time = str(infor_pos.p.string) 
infor_author = [str(x.string) for x in infor_pos.find_all('span', class_='author')]

# 获取介绍和正文
content_pos = pos.find('div', class_='announcement-stories__idea-story-description as-description')
intro_pos, conver_pos = content_pos.find_all('div', class_='field__item field--item-text_block')

intro = ''.join( map(str, intro_pos.find_all('p')) )
intro = re.sub('<p.*?>', '', str(intro))
intro = re.sub('</p>', '\n\n', intro)

conver = ''.join( map(str, conver_pos.find_all("p")) )
conver = re.sub('<p.*?>', '', str(conver))
conver = re.sub('</p>', '\n\n', conver)

print("获取标题、总结、时间、作者、介绍以及正文完成！等待写入tex文件")


# In[5]:


# tex文件模板
temple = """\\documentclass{article}
\\usepackage[UTF8]{ctex}
\\usepackage{hyperref}

\\linespread{1.3}
\\setlength{\parskip}{0.5em}
\\setlength{\parindent}{0em}

\\begin{document}

\\section*{%s}

%s

\\begin{flushright}
    \\textit{%s}
\\end{flushright}

%s

\\end{document}
"""

# 格式化内容并写入subscript.tex
infor = infor_time + ' | by ' + ' '.join(infor_author)

content = intro +'''\\vspace{1em}
\\large{\\textbf{TRANSCRIPT}}
\\vspace{1em}
\n\n
''' +conver
content = re.sub("<em>(.*?)</em>", "\\\\textsl{\\1}", content)
content = re.sub("<strong>(.*?)</strong>", "\\\\textbf{\\1}", content)
content = re.sub('<a href=\"(.*?)\">(.*?)</a>', "\\\\href{\\1}{\\2}", content)

tex = temple % (title, summary, infor, content)

with open("subscript.tex", "w+", encoding="utf-8") as f:
    f.write(tex)
    
print("将内容写入tex文件成功！等待编译pdf")


# In[6]:


get_ipython().system('xelatex subscript.tex')
get_ipython().system('del *.aux *.log *.out')
print("编译subscript.pdf成功！等待发送邮箱")


# In[7]:


# 转化为.py脚本
get_ipython().system('jupyter nbconvert --to script "scrapy the subscript.ipynb"')
# 将必要变量存入json文件
with open("./info.json", "a", encoding='utf-8') as f:
    json.dump({"title":title, "summary":summary}, f)

