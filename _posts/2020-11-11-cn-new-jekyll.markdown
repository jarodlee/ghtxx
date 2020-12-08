---
layout: post
title:  "hello world!"
date:   2020-11-11 09:38:51 +0800
categories: jekyll update
---
很高兴的采用jekyll，现在可以愉快的书写了，在ubuntu中，通过简单的安装几个工具，就可以在github上得到一个书写的平台，今天发现github上传的单个文件大小不能超过`25M`,所以大点的文件还是要通过ＡＱＦＴ这个工具来分享的。

Jekyll 现在要求写的博客命令方式如下:

`YEAR-MONTH-DAY-title.MARKUP`

其中 `YEAR` 是４位数字, `MONTH` and `DAY` 都是２位数字, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll 同时也加强了代码的语法高亮，比如下在的这段ruby代码:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
