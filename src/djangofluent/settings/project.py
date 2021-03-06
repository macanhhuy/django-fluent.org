"""
Project specific settings
"""
from .defaults import *

# Admins receive 500 errors, managers receive 404 errors.
ADMINS = (
    ('Edoburu', 'sysadmin@edoburu.nl'),
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'sysadmin@edoburu.nl'
EMAIL_SUBJECT_PREFIX = '[Django][djangofluent] '

# Database to use
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',  # or mysql
        'NAME':     'django-fluent.org',
        'USER':     'djangofluent',
        'PASSWORD': 'testtest',
    },
}

SECRET_KEY = '!k95k&wn43_8b5rp*c$+9pzcl=$w9s9o&t##x7os$3p3l%57&w'

# Apps to use
INSTALLED_APPS += (
    # Site parts
    'frontend',
    'apps.themeelements',
    'apps.wysiywg_config',

    # CMS parts
    'fluent_blogs',
    'fluent_blogs.pagetypes.blogpage',
    'fluent_pages',
    'fluent_pages.pagetypes.fluentpage',
    'fluent_pages.pagetypes.flatpage',
    'fluent_pages.pagetypes.redirectnode',
    'fluent_comments',
    'fluent_contents',
    'fluent_contents.plugins.code',
    'fluent_contents.plugins.commentsarea',
    'fluent_contents.plugins.gist',
    'fluent_contents.plugins.oembeditem',
    'fluent_contents.plugins.picture',
    'fluent_contents.plugins.sharedcontent',
    'fluent_contents.plugins.rawhtml',
    'fluent_contents.plugins.text',

    # Support libs
    'any_imagefield',
    'any_urlfield',
    'axes',
    'categories',
    'categories.editor',
    'crispy_forms',
    'django_wysiwyg',
    'django.contrib.comments',
    'filebrowser',
    'google_analytics',
    'mptt',
    'polymorphic',
    'polymorphic_tree',
    'sorl.thumbnail',
    'taggit',
    'taggit_autocomplete_modified',
    'threadedcomments',
    'tinymce',

    # and enable the admin
    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES += (
    'axes.middleware.FailedLoginMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'frontend.context_processors.frontend',
)

FORMAT_MODULE_PATH = 'djangofluent.settings.locale'  # Consistent date formatting


## -- Third party app settings

ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

COMMENTS_APP = 'fluent_comments'

DJANGO_WYSIWYG_FLAVOR = 'tinymce_advanced'
#DJANGO_WYSIWYG_MEDIA_URL = STATIC_URL + 'frontend/vendor/tiny_mce/'

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.png', '.gif'],
    'Document': ['.pdf', '.doc', '.xls', '.csv', '.docx', '.xlsx'],
    'Video': ['.swf', '.mp4', '.flv', '.f4v', '.mov', '.3gp'],
}
FILEBROWSER_EXCLUDE = ('cache',)  # sorl.thumbnail generated files
FILEBROWSER_MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # in bytes

FLUENT_BLOGS_BASE_TEMPLATE = 'base_blog.html'
FLUENT_BLOGS_ENTRY_LINK_STYLE = '/{year}/{month}/{slug}/'
FLUENT_BLOGS_INCLUDE_STATIC_FILES = False

FLUENT_CONTENTS_CACHE_OUTPUT = True

FLUENT_COMMENTS_EXCLUDE_FIELDS = ('url',)

FLUENT_DASHBOARD_APP_ICONS = {}
FLUENT_DASHBOARD_DEFAULT_MODULE = 'ModelList'

#FLUENT_OEMBED_SOURCE = 'noembed'

FLUENT_PAGES_BASE_TEMPLATE = 'base_flatpage.html'  # for fluent_pages.pagetypes.flatpage
FLUENT_PAGES_TEMPLATE_DIR = os.path.join(SRC_DIR, 'frontend', 'templates')

FLUENT_TEXT_CLEAN_HTML = True
FLUENT_TEXT_SANITIZE_HTML = True


## -- Site app settings

PACKAGEITEM_INTERNAL_GITHUB_ORG = 'edoburu'
