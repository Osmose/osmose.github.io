#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Kelly'
SITENAME = u'Michael Kelly <Osmose>'
SITEURL = ''
DISQUS_SITENAME = 'mkelly'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/Osmose'),
    ('Github', 'https://github.com/Osmose/'),
)

DEFAULT_PAGINATION = False

THEME = 'themes/tuxlite_tbs'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
