#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diego Volpatto'
SITENAME = u'Engimathics'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Fortaleza'

DEFAULT_LANG = 'pt_BR.utf8'
LOCALE = ('pt_BR.utf8')

USE_FOLDER_AS_CATEGORY = True

#THEME = 'html5-dopetrope'
THEME = '/home/volps/pelican-themes/voidy-bootstrap'
MAIL = 'volpatto@lncc.br'
FACEBOOK_USER = 'diego.volpatto'
GOOGLEPLUS_USER = '111987548001471824619'

ABOUT_IMAGE = './content/images/olocobixo.jpg'

#ABOUT_TEXT = 'Divagações bastante informais sobre matemática computacional, engenharia (particularmente Química e Mecânica) e coisitas mais que achar interessante por aí! Ocasionalmente, publicarei algumas notas pessoais que tenha desenvolvido.'
SITESUBTITLE = 'Divagações bastante informais sobre matemática computacional, engenharia (particularmente Química e Mecânica) e coisitas mais que achar interessante por aí! Ocasionalmente, publicarei algumas notas pessoais que tenha desenvolvido.'

COPYRIGHT = 'Diego Tavares Volpatto'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sidebar
SIDEBAR = "sidebar.html"
CUSTOM_SIDEBAR_MIDDLES = ("sb_links.html", "sb_taglist.html", )

# Blogroll
LINKS = (('LNCC', 'http://lncc.br/'),
         ('Python.org', 'http://python.org/'))
#         ('Jinja2', 'http://jinja.pocoo.org/'),

# Social widget
SOCIAL = (('Google+', 'http://plus.google.com/111987548001471824619',
         'fa fa-google-plus-square fa-fw fa-lg'),
        ('LinkedIn', 'https://www.linkedin.com/in/diego-volpatto-1a286068/',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('Facebook', 'https://www.facebook.com/diego.volpatto',
         'fa fa-facebook-square fa-fw fa-lg'),
        ('GitHub', 'https://github.com/volpatto',
         'fa fa-github-square fa-fw fa-lg'),
        )
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Markup and plugin config

#MARKUP = ('md', 'ipynb')
MARKUP = ('md', 'ipynb')

STATIC_PATHS = ['images']
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
#PLUGINS = ['ipynb.liquid']
IPYNB_IGNORE_CSS=False
IPYNB_USE_META_SUMMARY=True

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "volps.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
