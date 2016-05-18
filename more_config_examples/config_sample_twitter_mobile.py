# coding=utf-8
# 这是为twitter(手机站)镜像配置的示例配置文件 (为了减少代码冗余, 一部分没有修改的设置直接引用了上层目录 config_sample.py )
# 各项设置选项的详细介绍请看 config_sample.py 中对应的部分
# 本配置文件假定你的服务器本身在墙外
# 如果服务器本身在墙内(或者在本地环境下测试, 请修改`Proxy Settings`中的设置(在PC站的配置文件中)
#
# 由于twitterPC和twitterMobile实际上是相互独立的, 而且由于逻辑非常复杂, 即使使用镜像隔离功能, 也会导致手机站不正常
#   所以把twitterPC和twitterMobile分成两个配置文件
# 使用本配置文件运行的twitter镜像, 支持所有的twitter功能(暂时还没发现不能用的功能)

# 导入未修改的配置, 减少冗余
from config_sample import *

# 由于很多设置跟twitterPC一样,所以从twitterPC的配置文件导入
from .config_sample_twitter_pc import *

# ############## Local Domain Settings ##############
my_host_name = 'localhost'
my_host_scheme = 'http://'

# ############## Target Domain Settings ##############
target_domain = 'mobile.twitter.com'
target_scheme = 'https://'

# 删除 mobile.twitter.com, 添加 twitter.com
external_domains.remove('mobile.twitter.com')
external_domains.append('twitter.com')

# 其他设置都跟twitterPC站配置文件相同