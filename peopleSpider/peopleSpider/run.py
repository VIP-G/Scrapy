from scrapy import cmdline

name = 'pps'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())

# lpush pps:start_urls http://politics.people.com.cn/GB/1024/index1.html

