# the subscript of podcast *TFTS* 

> when I listen the podcast *think fast talk smart* on the spotify, I found it is so interesting and useful material for me to learn English.(exactly, you could find my poor English through the text (*/ω＼*), I really want to lean English well.)
>
> But I  think that I really need the subscript of  podcast *TFTS*, so, why don't make a program to help me to do that? 
>
> Come on, let's do it!

the steps :

1. crawl the original subscript.	(crawl)
3. format as a LaTex file.    (LaTex template)
4. transfer to pdf file.    (call the compile command)
5. sent to me.    (email)

-----

## Crawl the Original Subscript

> I choose the python's module "[urllib3](https://urllib3.readthedocs.io/en/stable/user-guide.html)" to get the webpage and "[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id9)" to parser it.

the [TFTS website](https://www.gsb.stanford.edu/business-podcasts/think-fast-talk-smart-podcast) stored subscripts of all episodes. And all we need to do , is let python to crap the subscript of the newest episode( or other episode is ok). 



---

## Format as A LaTex File

When I scrapy the text I want, the next thing is to format it to a standered .tex file, and I use the template as fallowing:

```tex
\\documentclass{article}
\\usepackage[UTF8]{ctex}
\\usepackage{hyperref}

\\linespread{1.3}
\\setlength{\parskip}{0.5em}
\\setlength{\parindent}{0em}

\\begin{document}

\\section*{title}

summary

\\begin{flushright}
    \\textit{infor}
\\end{flushright}

content

\\end{document}
```

So, I just need to format the "title"，”summary“，”infor“ and "content".

However, at least for me, the difficult is the "content" part, and I choose use ```re.sub``` to replace the ```<em>```, ```<stong>``` and ```<a href="">``` tag with ```\textsl{}```, ```\textbf{}``` and ```\hyref{}{}```.



---

## Transfer to pdf file

Normally, compared with LaTex IDE (like TexStudio ), Commands to compile .tex file looks more difficult and complex. 

Thank God ! we don't need too much deep technique, just a command line ```xelatex script.tex``` is OK.

What? You even didn't install the LaTex yet! oh my dear~ so, [install and config LaTex ](https://www.bilibili.com/video/BV1p44y1P7P4/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=f2260db80eec1196bb01aa75098d22a8), take it, no thanks.

---

## Sent to Me

> python standerd module to create email and sent email is [email](https://docs.python.org/zh-cn/3/library/email.html#module-email) and [smtpib](https://docs.python.org/zh-cn/3/library/smtplib.html#module-smtplib)



# files introduction

```scrapy the subscript.ipynb```: the program finish the first three steps, but .ipynb file.

```send_mail.py```:  the program finish the last steps.

```subscript.tex```: the generated .tex file.

```subscript.pdf```: the complied .pdf file.

```info.json```: some information about the episode we scrapied, which used to help send email better.

```account.json```: Emm.... Not surprisingly, you couldn't find this file, if you do, email me soon, Otherwise there will be a terrible thing to happen.(just a cold joke, the file is my contains my email password, used to log in the email server)

```main.py```: mian .py file, which joint ```scrapy the subscript.ipynb``` and ```send_mail.py``` , you can only use commond ```ipython main.py``` to finish the goal.













