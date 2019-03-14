FROM python:3.6

# 创建工作目录
RUN mkdir /my_blog  

#设置工作目录
WORKDIR /my_blog

#将当前目录加入到工作目录中
ADD . /my_blog
RUN pip3 install -r requirements.txt
#对外暴露端口
EXPOSE 80 8080 8000 5000
#设置环境变量
ENV SPIDER=/my_blog \