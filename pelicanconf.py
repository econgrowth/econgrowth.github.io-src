#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

from pelican_jupyter import markup as nb_markup

DELETE_OUTPUT_DIRECTORY = False
# Me
AUTHOR = u'Ömer Özak'
AUTHORS = u'Ömer Özak'
SITENAME = u'Economic Growth and Comparative Development'
SITEURL = 'https://econgrowth.github.io'
FAVICON = 'images/favicomatic/favicon.ico'
#SITELOGO = 'images/Depression.jpg'
#SITELOGO_SIZE = 100
#BANNER = '/images/cropped-escher2-990x1804.jpg'
#BANNER_SUBTITLE = 'Ömer Özak'
#BANNER_ALL_PAGES = True

PATH = 'content'

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'
DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Feeds
FEEDS =  (('All posts', 'feeds/all.atom.xml'),
          ('Category', 'feeds/category'),
          ('OPW', 'feeds/tag/opw.atom.xml'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/econgrowth'),
          ('Twitter', 'https://twitter.com/OmerOzakEcon'),
          ('Linkedin', 'https://linkedin.com/in/omerozak'),
          ('Researchgate','https://www.researchgate.net/profile/Oemer_Oezak'),)

# Github
GITHUB_USER = 'econgrowth'
GITHUB_SHOW_USER_LINK = 'True'
GITHUB_REPO_COUNT = 2

# Blogroll
LINKS = (('Ömer Özak', 'http://omerozak.com/'),
         ('Dept. Economics', 'http://www.smu.edu/economics'),
         ('SMU', 'http://www.smu.edu/'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

####################################################
# Additions
# tell pelican where your custom.css file is in your content folder
STATIC_PATHS = ['images', 'downloads', 'notebooks', 'pdf', 'extra/main.css',
                'extra/font-awesome', 'extra/custom.css',
                'downloads/files','downloads/code', 'images/favicon.ico', 'images/pics']
# tell pelican where it should copy that file to in your output folder
EXTRA_PATH_METADATA = {
    'extra/main.css': {'path': 'theme/css/main.css'},
    'extra/custom.css': {'path': 'static/custom.css'},
}
# tell the pelican-bootstrap-3 theme where to find the custom.css file in your output folder
CUSTOM_CSS = 'static/custom.css'

READERS = {'html': None}

CODE_DIR = 'notebooks/'
NOTEBOOK_DIR = 'notebooks/'
IPYNB_NB_SAVE_AS = 'notebooks/'

# Technical stuff
# THEME
#THEME = '../../pelican-themes/chameleon'
THEME = 'pelican-themes/pelican-bootstrap3'
#THEME = '../../pelican-themes/bootstrap2'
#JINJA_EXTENSIONS = ['jinja2.ext.i18n']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'simplex'

# PLUGINS
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['../../pelican-plugins']
PLUGINS = ['render_math', 'ipynb.markup', 'i18n_subsites',
           'summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'tag_cloud', 'pelican_javascript',
            'liquid_tags.include_code', 'ipynb.liquid',
           'liquid_tags.literal']
macros = ['/home/user/latex-macros.tex']

# ipynb
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True

# MATH_JAX
MATH_JAX = {'color': 'blue', 'align': 'left', 'macros': macros}
MATH_JAX = {'tex_extensions': ['color.js','mhchem.js']}

#THEME = 'notmyidea'
PYGMENTS_STYLE='default'
#PYGMENTS_STYLE='friendly'

#For pelican-bootstrap3
#BOOTSTRAP_THEME='simplex'
#BOOTSTRAP_THEME='yeti'
#BOOTSTRAP_THEME='superhero' #nice but, background doesn't work well with code as is
#BOOTSTRAP_THEME='cosmo' #used for T&P through 2016
BOOTSTRAP_THEME='slate'

# using Bootswatch Flatly
BS3_THEME = 'http://bootswatch.com/slate/bootstrap.min.css'
BS3_THEME_NAME = 'Slate'
BS3_THEME_HOMEPAGE = 'http://bootswatch.com/slate/'
BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css'
BS3_JS  = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js'

'''
BOOTSTRAP_THEME='flatly' #looks good, some color
#BOOTSTRAP_THEME='journal' #also looks good, more B&W
#BOOTSTRAP_THEME='readable'

#BOOTSTRAP_THEME='paper'
DISPLAY_BREADCRUMBS=False
BOOTSTRAP_NAVBAR_INVERSE=False
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_BADGE = True
DISPLAY_TAGS_ON_SIDEBAR=True
TAG_CLOUD_MAX_ITEMS=25
DISPLAY_TAGS_INLINE=True
HIDE_SIDEBAR=False
'''

LOAD_CONTENT_CACHE = False

# Structure of menubar
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Syllabus', '/pages/Syllabus.html'),
    ('Reading List', '/pages/Reading List.html'),
    ('Lecture Notes', '/pages/Lecture Notes.html'),
    ('Computation', '/pages/Computation.html'),
    ('Useful Tips', '/pages/Useful Tips.html'),
    ('CV', '/pages/CV.html'),
    ('Contact', '/pages/Contact.html'),
#    ('Email', 'http://www.google.com/recaptcha/mailhide/d?k=01Mcn4h5MJg-nEwpTtN4oQVg==&c=5mZN5MlTpATyB-iUqDo8FQ=='),
    )

# License
CC_LICENSE = "CC-BY-NC-SA"

# Sharing
ADDTHIS_PROFILE = 'ra-586c25633fd6ba9b'
