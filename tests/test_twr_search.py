#!/usr/bin/env python
#
# Copyright (c) 2013 Martin Abente Lahaye. - tch@sugarlabs.org

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import sys

from gi.repository import GObject

sys.path.append("..")
from twitter.twr_search import TwrSearch
from twitter.twr_account import TwrAccount


consumer_key = ''
consumer_secret = ''

access_key = ''
access_secret = ''

TwrAccount.set_secrets(consumer_key, consumer_secret,
                       access_key, access_secret)


def __phase1_failed_cb(search, info):
    print '[FAILED] phase1: tweets-downloaded-failed, with %s' % info
    loop.quit()


def __phase1_cb(search, info):
    print '[OK] phase1: tweets-downloaded, count: %s' % len(info['statuses'])
    loop.quit()


search = TwrSearch()
search.connect('tweets-downloaded', __phase1_cb)
search.connect('tweets-downloaded-failed', __phase1_failed_cb)
search.tweets('@tchx84', count=1)

loop = GObject.MainLoop()
loop.run()