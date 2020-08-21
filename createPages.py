import os
import json
import shutil
import random
import hashlib
import markdown
from urllib import parse
from bs4 import BeautifulSoup


title_list = []
md_files_path = 'mdFiles/'
img_path_in_md_file = 'index_files/'

def main():
	convert_md_to_blog_html()
	create_title_json()
	create_post_list_html()
	shutil.copyfile('template/about.html', 'blogPages/about.html');

def convert_md_to_blog_html():
	md_text = ''
	html_text = ''
	template_html = ''
	with open('template/template.html',encoding="utf8") as f:
	    template_html = f.read()
	f.close()

	for file in os.listdir(md_files_path) :
		if file == 'images' :
			continue
		date = file[:9]
		title_list.append(file)
		with open(md_files_path + file,encoding="utf8") as t_f:
			md_text = t_f.read()
			html_text = markdown.markdown(md_text,extensions=['fenced_code'])
		t_f.close()

		html_text = html_text.replace(img_path_in_md_file, '../images/')
		article_html = template_html.replace('[articleHtml]', html_text)
		index = file.find('.')
		title = file[11:index]
		article_html = article_html.replace('[title]', title)
		articleId = hashlib.md5(title.encode("utf-8")).hexdigest()
		article_html = article_html.replace('[articleId]', articleId)
		article_html = article_html.replace('[articleTitle]', title)
		new_html_file = open('blogPages/articles/' + title + '.html','wb+')
		new_html_file.write(bytes(article_html,'utf8'))
		new_html_file.close()

def create_title_json():
	title_list.sort()
	json_file = open('blogPages/titles.json','wb+')
	json_file.write(bytes('[\n','utf8'))
	title_list.reverse()
	for i,t in enumerate(title_list) :
		date = t[:10]
		index = t.find('.')
		title = t[11:index]
		json_object = '{"date":"' + date + '","title":"' + title + '"}'
		if i != len(title_list) - 1 :
			json_object += ',\n'
		json_file.write(bytes(json_object,'utf8'))
	json_file.write(bytes('\n]\n','utf8'))
	json_file.close()


def create_post_list_html():
	json_data = ''
	title_html = ''
	postList_html = ''
	title_list_html = ''
	title_html_template = "<div class='item'><div class='content'><lable class='dtLable'>[date]</lable>&nbsp;&nbsp;&nbsp;&nbsp;<a href='articles/[encodeTitle].html?n=[randomNum]'>[title]</a></div></div>"

	with open('blogPages/titles.json', encoding="utf8") as json_f:
		json_data = json.load(json_f)
	json_f.close()

	title_list.reverse()
	for item in json_data :
		date = item['date']
		title = item['title']
		encodeTitle = parse.quote(title)
		title_html = title_html_template.replace('[date]',date)
		title_html = title_html.replace('[title]',title)
		title_html = title_html.replace('[encodeTitle]',encodeTitle)
		title_html = title_html.replace('[randomNum]',str(random.random()))
		title_list_html += title_html

	with open('template/postListTemplate.html',encoding="utf8") as t_f:
	    postList_html = t_f.read()
	t_f.close()
	postList_html = postList_html.replace('[titleList]',title_list_html)
	new_html_file = open('blogPages/postList.html','wb+')
	new_html_file.write(bytes(postList_html,'utf8'))
	new_html_file.close()


	with open('template/index.html',encoding="utf8") as t_f:
	    postList_html = t_f.read()
	t_f.close()
	postList_html = postList_html.replace('[titleList]',title_list_html)
	new_html_file = open('blogPages/index.html','wb+')
	new_html_file.write(bytes(postList_html,'utf8'))
	new_html_file.close()

main()
