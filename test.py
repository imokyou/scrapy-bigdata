# -*- coding: utf-8 -*-
import urlparse

url = 'http://www.zhihu.com/question/23238816#answer-4843588'
result = urlparse.urlparse(url)
print result.fragment
if 'answer' not in result.fragment:
    print 'haha!'
print result.path.split('/')[2]


list1 = [u'\n\n',u'\n\n',u'\n']
if not list1:
    print 111
else:
    print 2


def stripN(lst):
    result = []
    for i in lst:
        result.append(i.replace('\n',''))
    return result

print stripN(list1)