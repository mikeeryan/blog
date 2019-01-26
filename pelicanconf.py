#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michael Eryan'
SITENAME = 'Personal Blog'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages'] # where About goes
ARTICLE_PATHS = ['posts']  # where .mds are

# order the posts? default is by creation date, not modified
# ARTICLE_ORDER_BY = 'attribute'
# PAGE_ORDER_BY = 'attribute'

# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'  # change from English

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FAVICON = '/extra/favicon.ico'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['pelican-plugins']

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

I18N_TEMPLATES_LANG = 'en'

MARKUP = ('md', 'ipynb', 'html')

#Ignore all files that start with a dot .
IGNORE_FILES = ['.*','*-checkpoint.ipynb']

PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup'
	] 

# cannot make the search work though, so remove 'tipue_search'
	
# CODE_DIR = 'code'	
# NOTEBOOK_DIR = 'code'  # he had posts - and .md's in there

# to grab metada from a cell in the notebook
# IPYNB_USE_METACELL = True # not taking effect, still wants metada inside the .ipynb
	
# for Tique Search Plugin
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

# for the custom css files - Pelican does not create "static"?
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'
# what kind of paths are these? - pelican copies from extra to output
# but it is not working?

STATIC_PATHS = [ 'extra' ]  # dir under root

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}