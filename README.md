# Generate Blog pages
Convert markdown files to HTML pages,and create a simple blog site by server these static pages.

Online blog pages demo : https://tocu.me
## Requirements
- Python3  
- python3-markdown  
- bs4(BeautifulSoup)

## Generate pages
Execute the follow commands,example in Fedora
```shell
sudo dnf install python3-markdown.noarch
sudo pip3 install bs4  
git clone https://github.com/uxov/generateBlogPags.git
cd generateBlogPags
```
Before convert
1. Put markdown files under `generateBlogPags/mdFiles` directory
2. Put all images in `generateBlogPags/mdFiles/images`

Then
```shell
sh generate.sh
```
And the HTML pages will in `generateBlogPags/blogPages/articles`

## Create a simple blog
server the `generateBlogPags/blogPages` directory by HTTP server,like Nginx.

## About blog comment
In my case,I use [blogCommentServer](https://github.com/uxov/blogCommentServer) to create the comment server.
