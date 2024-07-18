import captcha

project = 'Captcha'
copyright = '2013, Hsiaoming Yang'
author = 'Hsiaoming Yang'

master_doc = 'index'

# The full version, including alpha/beta/rc tags
version = captcha.__version__
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx_sitemap",
]

extlinks = {
    'pull': ('https://github.com/lepture/captcha/pull/%s', 'pull request #%s'),
    'issue': ('https://github.com/lepture/captcha/issues/%s', 'issue #%s'),
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

html_baseurl = "https://captcha.lepture.com/"
sitemap_url_scheme = "{link}"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_static_path = ["_static"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'shibuya'
html_theme_options = {
    "accent_color": "green",
    "light_logo": "_static/light-logo.svg",
    "dark_logo": "_static/dark-logo.svg",
    "twitter_site": 'lepture',
    "twitter_creator": 'lepture',
    "twitter_url": 'https://twitter.com/lepture',
    "github_url": 'https://github.com/lepture/captcha',
    "carbon_ads_code": "CE7DKK3W",
    "carbon_ads_placement": "captchalepturecom",
    "og_image_url": "https://captcha.lepture.com/_static/icon.png",
    "nav_links": [
        {"title": "Sponsor me", "url": "https://github.com/sponsors/lepture"},
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

html_copy_source = False
html_show_sourcelink = False

html_favicon = "_static/icon.svg"

html_context = {
    "source_type": "github",
    "source_user": "lepture",
    "source_repo": "captcha",
}
