# Site metadata
SITENAME = 'kbits-theme-demo'
SITESUBTITLE = "Demonstration of kbits-theme for Pelican"
AUTHOR = 'John T. Wodder II'
DEFAULT_LANG = 'en'
TIMEZONE = 'America/New_York'
LOCALE = 'en_US.UTF-8'


# Site input layout
PATH = 'src'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['static']
IGNORE_FILES = ['.*.swp']
USE_FOLDER_AS_CATEGORY = False


# Site output layout
OUTPUT_PATH = 'build'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{slug}/{lang}/'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + 'index.html'

ARCHIVES_SAVE_AS = 'posts/index.html'
YEAR_ARCHIVE_URL = 'posts/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = YEAR_ARCHIVE_URL + 'index.html'
MONTH_ARCHIVE_URL = 'posts/{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = MONTH_ARCHIVE_URL + 'index.html'

DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = DRAFT_URL + 'index.html'
DRAFT_LANG_URL = 'drafts/{slug}/{lang}/'
DRAFT_LANG_SAVE_AS = DRAFT_LANG_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_LANG_URL = '{slug}/{lang}/'
PAGE_LANG_SAVE_AS = PAGE_LANG_URL + 'index.html'

DRAFT_PAGE_URL = 'drafts/{slug}/'
DRAFT_PAGE_SAVE_AS = DRAFT_PAGE_URL + 'index.html'
DRAFT_PAGE_LANG_URL = 'drafts/{slug}/{lang}/'
DRAFT_PAGE_LANG_SAVE_AS = DRAFT_PAGE_LANG_URL + 'index.html'

AUTHOR_URL = 'authors/{slug}/'
AUTHOR_SAVE_AS = AUTHOR_URL + 'index.html'
AUTHORS_SAVE_AS = 'authors/index.html'

CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'
TAGS_SAVE_AS = 'tags/index.html'

DEFAULT_PAGINATION = 5

PAGINATION_PATTERNS = [
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
]


# Building & formatting settings
CACHE_CONTENT = False
STATIC_CHECK_IF_MODIFIED = True

DOCUTILS_SETTINGS = {
    "smart_quotes": True,
    "math_output": "mathjax irrelevant.value",
}

SLUGIFY_SOURCE = 'basename'
PAGE_ORDER_BY = 'title'
DEFAULT_CATEGORY = 'Miscellanea'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M %z'

# <https://github.com/getpelican/pelican/pull/2785>
FORMATTED_FIELDS = ['summary', 'Summary', 'Source']


# Plugins
#PLUGINS = ['plugins.autopages']

# autopages
AUTHOR_PAGE_PATH = f'{PATH}/authors'
CATEGORY_PAGE_PATH = f'{PATH}/categories'
TAG_PAGE_PATH = f'{PATH}/tags'


# Themes
THEME = './theme'


# Theme variables
USE_MATHJAX = True
#MATHJAX_CONFIG = ???
GITHUB_SOURCE_URL = 'https://github.com/jwodder/kbits-theme-demo'
PATH_IN_REPO = PATH  # PATH relative to root of repository
SHOW_AUTHOR = True
SHOW_AUTHOR_IN_LISTINGS = True

FOOTER_HTML = '''
Made with <a href="https://getpelican.com/">Pelican</a> and the <a
href="https://github.com/jwodder/kbits-theme">kbits-theme</a>
'''

DISPLAY_CATEGORIES_ON_MENU = False

MENU_NAME = 'Site Menu'

MENUITEMS = [
    ('Archives', 'posts/'),
    ('Authors', 'authors/'),
    ('Categories', 'categories/'),
    ('Tags', 'tags/'),
    ('Site Repository', 'https://github.com/jwodder/kbits-theme-demo'),
]

PAGES_MENU = True
PAGES_MENU_NAME = 'Site Pages'
CATEGORIES_MENU = True
CATEGORIES_MENU_NAME = 'Site Categories'

EXTRA_MENUS = [
    ('Site Building Blocks', [
        ('GitHub Pages', 'https://pages.github.com'),
        ('Pelican', 'https://getpelican.com'),
        ('kbits-theme', 'https://github.com/jwodder/kbits-theme'),
        ('Python', 'https://www.python.org'),
        ('Jinja', 'http://jinja.palletsprojects.com'),
        ('HTML', 'https://en.wikipedia.org/wiki/HTML'),
        ('CSS', 'https://www.w3.org/Style/CSS/'),
        ('reStructuredText', 'https://docutils.sourceforge.io/rst.html'),
    ]),
]

EXTRA_METADATA_FIELDS = [
    ('Address', 'address'),
    ('Contact', 'contact'),
    ('Organization', 'organization'),
    ('Revision', 'revision'),
    ('Version', 'version'),
    ('Translator', 'translator'),
    ('Source', 'source'),
    ('Copyright', 'copyright'),
]


# Variables to leave unset during development:
SITEURL = ''
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Other
BIND = '127.0.0.1'
