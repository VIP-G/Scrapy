from scrapy import cmdline

name = 'jd'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
# lpush jd:start_urls https://mall.jd.com/index-1000015441.html?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=113098950926_0_f4806f9c0e2e48bab760aa196dddf56c