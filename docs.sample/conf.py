import os
import sys
import time
import re
import pkgutil
import string
import f5_sphinx_theme

CURDIR = os.path.abspath(os.path.dirname(__file__))
# -*- coding: utf-8 -*-
#
#
# BEGIN CONFIG
# ------------
#
# REQUIRED: Your class/lab name

# OPTIONAL: The URL to the GitHub Repository for this class
show_source = True
html_show_sourcelink = True
html_copy_source = True
html_permalinks = False
html_show_sphinx = False
hoverxref_auto_ref = True
autosectionlabel_prefix_document = True
copybutton_prompt_text = "$ "
copybutton_only_copy_prompt_lines = True
copybutton_remove_prompts = True
extlinks_detect_hardcoded_links = True
sphinx_tabs_disable_css_loading = False
nitpicky = True

hoverxref_roles = [
    'numref',
    'confval',
    'setting',
    'term',
]


#
# END CONFIG
# ----------

sys.path.insert(0, os.path.abspath("."))

rst_prolog = open(os.path.join(CURDIR, 'rst_prolog.inc'),'r').read()
rst_epilog = open(os.path.join(CURDIR, 'rst_epilog.inc'),'r').read()

#is_subproject=True
#readthedocs_url="https://f5-xc-workspaces.readthedocs.io/"

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.graphviz",
    "sphinxcontrib.nwdiag",
    "sphinx_copybutton",
    "sphinxcontrib.blockdiag",
    "sphinxcontrib.youtube",
    "sphinxcontrib.details.directive",
    "hoverxref.extension",
    "sphinx_toolbox.collapse",
    "sphinx_toolbox.code",
    "sphinx.ext.autosectionlabel",
    "sphinx_tabs.tabs",
    "sphinx-prompt",
    "sphinx_substitution_extensions",
    "sphinxcontrib.mermaid",
    "sphinx.ext.viewcode",
#    "subprojecttoctree",
    "sphinx_design"
]


html_theme_options = {
    'github_url': "https://github.com/robinmordasiewicz/f5-xc_cloud-and-edge-sites",
    "use_repository_button": True,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'top',
    'style_external_links': False,
    'vcs_pageview_mode': 'edit',
    'style_nav_header_background': '#f7f8fa',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'breadcrumbs': True,
    'body_centered': False,
    'globaltoc_includehidden': True,
    'sidebarwidth': '250',
    'titles_only': True,
    "show_toc_level": 4,
    "footer_items": ["last-updated"],
    "site_name": "Cloud and Edge Sites",
    "next_prev_link": True,
    "repository_url": "https://github.com/robinmordasiewicz/f5-xc_cloud-and-edge-sites",
    "github_url": "https://github.com",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "path_to_docs": "docs",
    "external_links": [
      {"name": "API Developer Portal", "url": "https://console.ves.volterra.io/web/devportal/domain"},
      {"name": "API Docs", "url": "https://docs.cloud.f5.com/docs/api"}
    ],
    "navbar_center": ["breadcrumbs"]
}

html_context = {
    "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "robinmordasiewicz",
    "github_repo": "f5-xc-iac",
    "github_version": "main",
    "doc_path": "docs",
}

html_title = "Cloud and Edge Sites"
html_logo = "images/logo_f5.svg"

graphviz_output_format = "svg"
graphviz_font = "DejaVu Sans:style=Book"
graphviz_dot_args = [
    "-Gfontname='%s'" % graphviz_font,
    "-Nfontname='%s'" % graphviz_font,
    "-Efontname='%s'" % graphviz_font,
]

diag_fontpath = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
diag_html_image_format = "SVG"
diag_latex_image_format = "PNG"
diag_antialias = False

blockdiag_fontpath = nwdiag_fontpath = diag_fontpath
blockdiag_html_image_format = nwdiag_html_image_format = diag_html_image_format
blockdiag_latex_image_format = nwdiag_latex_image_format = diag_latex_image_format
blockdiag_antialias = nwdiag_antialias = diag_antialias

eggs_loader = pkgutil.find_loader("sphinxcontrib.spelling")
found = eggs_loader is not None

if found:
    extensions += ["sphinxcontrib.spelling"]
    spelling_lang = "en_US"
    spelling_word_list_filename = "../wordlist"
    spelling_show_suggestions = True
    spelling_ignore_pypi_package_names = False
    spelling_ignore_wiki_words = True
    spelling_ignore_acronyms = True
    spelling_ignore_python_builtins = True
    spelling_ignore_importable_modules = True
    spelling_filters = []

source_parsers = {
    ".md": "recommonmark.parser.CommonMarkParser",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Workspaces"
author = "Robin Mordasiewicz"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ""
# The full version, including alpha/beta/rc tags.
release = ""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "links.rst"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
#pygments_style = 'github-dark'


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_emit_warnings = True
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# html4_writer = True
html_theme = "f5_sphinx_theme"
#html_theme = "pyramid"
#html_theme = "sphinx_rtd_theme"
#html_theme = "sphinx_book_theme"
#html_theme = "pydata_sphinx_theme"
#html_theme_path = f5_sphinx_theme.get_html_theme_path()
#html_sidebars = {"**": ["searchbox.html", "localtoc.html", "globaltoc.html"]}
html_sidebars = {
    "**": ["sidebar-nav-bs"]
}
#html_sidebars = {"**": ["custom-toc.html"]}
html_codeblock_linenos_style = 'table'

html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

extlinks = {
   'issue': ('https://github.com/f5devcentral/f5-agility-labs-xc/issues/%s','issue %s')
}


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"
]

