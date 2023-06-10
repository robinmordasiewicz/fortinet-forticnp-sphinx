# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FortiCNP'
copyright = '2023, Robin Mordasiewicz'
author = 'Robin Mordasiewicz'
release = 'Version 22.4a'
html_permalinks = False
html_show_sphinx = False

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
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
    "sphinx_design"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'logo.svg'
html_theme_options = {
    'prev_next_buttons_location': 'top',
    'style_external_links': False
}

html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
}

html_css_files = [
    'css/custom.css',
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"
]

html_context = {
  'display_github': True,
  'github_user': 'robinmordasiewicz',
  'github_repo': 'fortinet-forticnp',
  'github_version': 'main/docs/',
}
