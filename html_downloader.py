# coding=utf-8
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # 1.直接请求  response = urllib2.urlopen(url)

        '''   
        2.添加data、http header
        request = urllib2.Request(url)
        request.add_data('a', 1)
        request.add_header('User-Agent','Mozilla/5.0')
        response = urllib2.urlopen(request)
        '''
        '''
        3.添加特殊情景的处理器
        创建cookie容器
        cj = cookielib.CookieJar()
        创建一个opener
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        给urllib2安装opener
        urllib2.install_opener(opener)
        使用带有cookie的urllib2访问网页
        response = urllib2.urlopen(url)
        '''
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            print "请求的url响应失败:" + url
            return None
        return response.read()
