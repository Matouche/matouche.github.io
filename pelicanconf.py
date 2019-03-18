#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mathis Dubrul'
SITENAME = 'Mathis Dubrul'
SITESUBTITLE = "Animateur / Illustrateur 2D"
SITEURL = 'https://matouche.github.io'
SITE_DESCRIPTION = """Je suis étudiant en 3ème année à la Haute École Albert Jacquard en Animation et Illustration Numérique 2D."""

THEME = 'mportfolio'
FAVICON = 'images/favicon.png'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('<strong>Demo Reel</strong>', 'https://matouche.github.io/demo-reel-2018.html'),
	  ('Vimeo', 'https://vimeo.com/user12625616'),
          ('ArtStation', 'https://matouche.artstation.com'),
          ('CV', 'https://matouche.github.io/extra/specials/cv'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Useful settings :
DEFAULT_DATE = 'fs'
STATIC_PATHS = ['images', 'extra']
PAGE_EXCLUDES = ['extra']
ARTICLE_EXCLUDES = ['extra']
EXTRA_PATH_METADATA = {'extra/README.md' : {'path': 'README.md'},
                       'extra/specials/' : {'path': 'specials/'},}

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets']
