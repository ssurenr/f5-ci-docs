# -*- coding: utf-8 -*-
#
# F5 Container Integration documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 10 14:05:28 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import f5_sphinx_theme

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
#needs_sphinx = '1.5.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx_copybutton',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.doctest',
    'sphinxjp.themes.basicstrap',
    'cloud_sptheme.ext.table_styling',
    'sphinx.ext.extlinks'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = {
            '.rst': 'restructuredtext',
            '.txt': 'markdown',
            '.md': 'markdown',
       }

# The encoding of source files.
#
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'F5 Container Ingress Services'
copyright = u'2019 F5 Networks Inc'
author = u'F5 Networks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# External link shortcuts
extlinks = {'k8sdocs': ('https://kubernetes.io/docs/%s',
                      ''),
            'issues': ('https://github.com/F5Networks/f5-ci-docs/issue/%s',
                       'issue ')
            }

# All substitutions
# Try to keep sorted alphabetically
rst_epilog = """
.. |cfctlr| replace:: BIG-IP Controller
.. |cf-long| replace:: BIG-IP Controller for Cloud Foundry
.. |kctlr-long| replace:: BIG-IP Controller for Kubernetes
.. |kctlr| replace:: BIG-IP Controller
.. |mctlr-long| replace:: BIG-IP Controller for Marathon
.. |mctlr| replace:: BIG-IP Controller
.. |octlr-long| replace:: BIG-IP Controller for OpenShift
.. _Apache Mesos Marathon: https://mesosphere.github.io/marathon/
.. _Apache Mesos: https://mesosphere.com/
.. _Application labels for iApp mode: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/#application-labels-for-iapp-mode
.. _Application Manifest: https://docs.pivotal.io/pivotalcf/1-7/devguide/deploy-apps/manifest.html
.. _Better or Best license: https://f5.com/products/how-to-buy/simplified-licensing
.. _BIG-IP: https://f5.com/products/big-ip
.. _BIG-IP Application Security Manager: https://f5.com/products/big-ip/application-security-manager-asm
.. _BIG-IP Controller for Cloud Foundry: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/
.. _BIG-IP Controller for Kubernetes: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest
.. _BIG-IP Controller for Marathon: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest
.. _BIG-IP Local Traffic Management - Getting Started with Policies: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-local-traffic-policies-getting-started-13-0-0.html
.. _BIG-IP Local Traffic Management - Profiles Reference Guide: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-13-0-0.html
.. _BIG-IP partition: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-13-0-0/2.html
.. _BIG-IP Automap SNAT: https://support.f5.com/csp/article/K7820#types
.. _BIG-IP SSL profile: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-12-1-0/6.html
.. _BIG-IP System User Account Administration -> Administrative Partitions: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-12-0-0/3.html
.. _BIG-IP TMOS Routing Adminstration Guide: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-routing-administration-13-0-0/
.. _BIG-IP user account: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-13-0-0/1.html
.. _built-in middleware: %(base_url)s/products/asp/latest/#built-in-middleware
.. _cf-bigip-ctlr configuration parameters: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/#configuration-parameters
.. _cf-bigip-ctlr: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/
.. _cf-bigip-ctlr v1.1.0: %(base_url)s/products/connectors/cf-bigip-ctlr/v1.1/
.. _cf-bigip-ctlr reference documentation: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/
.. _cf-bigip-ctlr service broker config parameters: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/#broker-configs
.. _CIDR format: https://www.rfc-editor.org/info/rfc4632
.. _Cloud Foundry CLI: https://docs.cloudfoundry.org/cf-cli/getting-started.html
.. _Cloud Foundry: https://cloudfoundry.org/why-cloud-foundry/
.. _ClusterIP: https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/
.. _Cluster network: https://kubernetes.io/docs/concepts/cluster-administration/networking/
.. _Cluster Role Binding: https://kubernetes.io/docs/admin/authorization/rbac/#rolebinding-and-clusterrolebinding
.. _Cluster Role: https://kubernetes.io/docs/admin/authorization/rbac/#role-and-clusterrole
.. _Cluster: https://kubernetes.io/docs/tasks/administer-cluster/cluster-management/
.. _ConfigMap: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
.. _configuration parameters specific to OpenShift: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#openshift-sdn
.. _contact F5 support: https://f5.com/about-us/contact/regional-offices#regional-support
.. _Create a Kubernetes Secret containing your Docker login credentials: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
.. _Create a new namespace: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
.. _Create a new partition: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-implementations-12-1-0/29.html
.. _create and set a non-zero default Route Domain for a partition: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-implementations-13-0-0/4.html#guid-e73e1052-8e05-4913-bba3-99f29d26bc56
.. _DaemonSet: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
.. _DC/OS and DC/OS Enterprise: https://mesosphere.com/product/
.. _Deployment: https://kubernetes.io/docs/user-guide/deployments/
.. _Diego cell: https://docs.cloudfoundry.org/concepts/architecture/#diego-cell
.. _Disable automatic configuration sync on the DSC: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-device-service-clustering-administration-13-1-0/5.html
.. _Disable config sync for tunnels: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-tmos-tunnels-ipsec-13-1-0/2.html#GUID-5E1E2E56-0776-4B7A-A601-98C2C2E3775C
.. _Docker: https://www.docker.com/
.. _Express middleware: https://expressjs.com/en/guide/using-middleware.html
.. _Express: https://expressjs.com/
.. _F5 Docker registry: https://hub.docker.com/r/f5networks/
.. _F5 IPAM Controller: https://github.com/F5Networks/f5-ipam-ctlr
.. _f5-ipam-ctlr docs: %(base_url)s/products/ipam-ctlr/latest/
.. _F5 Resources: %(base_url)s/containers/v2/kubernetes/kctlr-f5-resource.html#f5-resource-properties
.. _F5 schema: https://github.com/F5Networks/k8s-bigip-ctlr/tree/master/schemas
.. _F5 virtual server properties: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#virtualserver-configmap-properties
.. _F5 Helm Chart: https://github.com/F5Networks/charts/tree/master/src/stable/f5-bigip-ctlr
.. _f5-bigip-ingress chart: https://github.com/F5Networks/charts/tree/master/src/stable/f5-bigip-ingress
.. _f5-kube-proxy reference documentation: %(base_url)s/products/connectors/f5-kube-proxy/latest/
.. _f5-kube-proxy: %(base_url)s/products/connectors/f5-kube-proxy/latest/
.. _flannel: https://github.com/coreos/flannel
.. _flannel manifest: https://github.com/coreos/flannel/blob/master/Documentation/kube-flannel.yml
.. _helm: https://helm.sh
.. _iApps: https://www.f5.com/products/f5-technologies
.. _iApp Pool Member table: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#iapp-pool-member-table
.. _Ingress annotations: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#ingress-resources
.. _Ingress controller: https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-controllers
.. _Ingress Resource: https://kubernetes.io/docs/concepts/services-networking/ingress/
.. _k8s-bigip-ctlr configuration parameters: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#controller-configuration-parameters
.. _k8s-bigip-ctlr iApp configuration parameters: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#iApp
.. _k8s-bigip-ctlr reference documentation: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/
.. _k8s-bigip-ctlr virtual server configuration parameters: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#virtualserver
.. _k8s-bigip-ctlr: %(base_url)s/containers/v2/kubernetes/
.. _k8s-bigip-ctlr v1.1.0-beta.1: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.1-beta/
.. _k8s-bigip-ctlr v1.1.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.1/
.. _k8s-bigip-ctlr v1.2.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.2/
.. _k8s-bigip-ctlr v1.3.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.3/
.. _k8s-bigip-ctlr v1.4.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.4/
.. _k8s-bigip-ctlr v1.5.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.5/
.. _kube-proxy: https://kubernetes.io/docs/admin/kube-proxy/
.. _kubectl: https://kubernetes.io/docs/user-guide/kubectl-overview/
.. _Kubernetes clusters: https://kubernetes.io/docs/concepts/cluster-administration/cluster-administration-overview/
.. _Kubernetes Dashboard: https://kubernetes.io/docs/user-guide/ui/
.. _Kubernetes Ingress controller: https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-controllers
.. _Kubernetes Ingress: https://kubernetes.io/docs/concepts/services-networking/ingress/
.. _Kubernetes node: https://kubernetes.io/docs/admin/node/
.. _Kubernetes RBAC documentation: https://kubernetes.io/docs/admin/authorization/rbac/
.. _Kubernetes Service: https://kubernetes.io/docs/user-guide/services/
.. _Kubernetes: https://kubernetes.io/
.. _local traffic management: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-basics-12-0-0.html
.. _Local Traffic Policies: https://support.f5.com/csp/article/K04597703
.. _Marathon Applications: https://mesosphere.github.io/marathon/docs/application-basics.html
.. _Marathon Apps: https://mesosphere.github.io/marathon/docs/application-basics.html
.. _Marathon Web Interface: https://mesosphere.github.io/marathon/docs/marathon-ui.html
.. _marathon-bigip-ctlr configuration parameters: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/#configuration-parameters
.. _marathon-bigip-ctlr iApp configuration parameters: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/#iApp
.. _marathon-bigip-ctlr reference documentation: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/
.. _marathon-bigip-ctlr: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/
.. _marathon-bigip-ctlr v1.1.0-beta.1: %(base_url)s/products/connectors/marathon-bigip-ctlr/v1.1-beta/
.. _marathon-bigip-ctlr v1.1.0: %(base_url)s/products/connectors/marathon-bigip-ctlr/v1.1/
.. _marathon-bigip-ctlr v1.3.0: %(base_url)s/products/connectors/marathon-bigip-ctlr/v1.3/
.. _Marathon: https://mesosphere.github.io/marathon/
.. _namespace: https://kubernetes.io/docs/user-guide/namespaces/
.. _namespaces: https://kubernetes.io/docs/user-guide/namespaces/
.. _NATS bus: https://docs.cloudfoundry.org/concepts/architecture/router.html#use
.. _NodePort: https://kubernetes.io/docs/concepts/services-networking/service/#nodeport
.. _oc: https://docs.openshift.com/enterprise/3.0/cli_reference/basic_cli_operations.html
.. _OpenShift F5 Router: https://docs.openshift.org/latest/install_config/router/f5_router.html
.. _OpenShift Route Annotations: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#supported-route-annotations
.. _OpenShift route resources: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#openshift-route-resources
.. _Overview of SNAT features: https://support.f5.com/csp/article/K7820
.. _Overview of the Standard Virtual Server: https://support.f5.com/csp/article/K93017176
.. _Pivotal Cloud Foundry: https://pivotal.io/platform
.. _Pod: https://kubernetes.io/docs/concepts/workloads/pods/pod/
.. _Pods: https://kubernetes.io/docs/concepts/workloads/pods/pod/
.. _Projects: https://docs.openshift.org/latest/architecture/core_concepts/projects_and_users.html#projects
.. _Red Hat OpenShift: https://www.openshift.com/container-platform/index.html
.. _Route annotations: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#supported-annotations
.. _Route configuration parameters: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#openshift-routes
.. _Route domain: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-routing-administration-13-0-0/8.html
.. _Secret: https://kubernetes.io/docs/user-guide/secrets/
.. _Self IP address: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-routing-administration-13-0-0/5.html#guid-52e1f1d8-9a6b-48cc-acfa-07745b757f07
.. _Service: https://kubernetes.io/docs/concepts/services-networking/service/
.. _ServiceAccount: https://kubernetes.io/docs/admin/service-accounts-admin/
.. _Service resources: https://kubernetes.io/docs/user-guide/services/
.. _Service Broker: https://docs.cloudfoundry.org/services/overview.html
.. _Set up two or more F5 BIG-IPs in a Device Service Cluster (DSC): https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-device-service-clustering-administration-13-1-0/11.html
.. _SNAT automap and self IP address selection: https://support.f5.com/csp/article/K7336
.. _Splunk: https://www.splunk.com/
.. _Static Pod: https://kubernetes.io/docs/admin/static-pods/
.. _store your Docker login credentials as a Secret: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
.. _supported Route configurations: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#supported-route-configurations
.. _system configuration: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-initial-configuration-12-0-0/2.html#conceptid
.. _Using flannel with Kubernetes: https://coreos.com/flannel/docs/latest/kubernetes.html
.. _F5 AS3 Extension: %(base_url)s/products/extensions/f5-appsvcs-extension/latest/
.. _F5 AS3 Extensions: %(base_url)s/containers/v2/kubernetes/kctlr-k8s-as3.html
.. _F5 AS3 Installation: %(base_url)s/products/extensions/f5-appsvcs-extension/latest/userguide/installation.html
.. _F5 AS3 User Guide: %(base_url)s/products/extensions/f5-appsvcs-extension/latest/userguide/
.. _F5 AS3 Reference Guide: %(base_url)s/products/extensions/f5-appsvcs-extension/latest/refguide/
.. _Container Ingress Services and AS3 Extension integration: %(base_url)s/containers/v2/kubernetes/kctlr-k8s-as3.html
.. _Updating the CIS trusted certificate store: %(base_url)s/kubernetes/kctlr-as3-cert-trust.html
.. _Overview of BIG-IP device certificates: https://support.f5.com/csp/article/K15664
.. _K16951115 Changing the BIG-IP DNS system device certificate using the Configuration utility: https://support.f5.com/csp/article/K16951115
.. _ReplicaSet: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
"""% {
    'base_url': 'https://clouddocs.f5.com'
}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build',
                    '_static/reuse',
                    'drafts',
                    'Thumbs.db',
                    '.DS_Store',
                    'venv',
                    '.github'
                    ]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'f5_sphinx_theme'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = f5_sphinx_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'next_prev_link': False
}

html_sidebars = {
    '**': ['searchbox.html', 'localtoc.html', 'globaltoc.html' ]
}


# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
#html_title = 'F5 Container Connectors'
html_title = 'F5 Container Ingress Services'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
#html_short_title = 'Container Connectors Home'
html_short_title = 'Container Ingress Services Home'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = '_static/f5-logo-solid-rgb_small.png'

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or
# 32x32 pixels large.
#
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static/']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = '%Y-%m-%d %I:%M:%S'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
html_domain_indices = True

# If false, no index is generated.
#
html_use_index = True

# If true, the index is split into individual pages for each letter.
#
html_split_index = False

# If true, links to the reST sources are added to the pages.
#
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = 'https://clouddocs.f5.com'

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'F5_Container Connectors_doc'

# -- Options for linkcheck ------------------------------------------------
# A list of regular expressions that match URIs that should not be checked when doing a linkcheck build. Example:
#linkcheck_ignore = [r'http://localhost:\d+/']

# The number of times the linkcheck builder will attempt to check a URL before declaring it broken. Defaults to 1 attempt.
linkcheck_retries = 2

# A timeout value, in seconds, for the linkcheck builder. The default is to use Python’s global socket timeout.
linkcheck_timeout = 5

linkcheck_anchors = False

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
      'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
      'pointsize': '12pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'F5_Container Connectors_doc.tex',
     u'F5 Container Connectors Documentation',
     'F5 Networks', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
latex_logo = '_static/f5-logo-solid-rgb_small.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# replaces latex_use_parts
# determines the topmost sectioning unit. It should be chosen from part,
#  chapter or section. The default is None; the topmost sectioning unit is
#  switched by documentclass. section is used if documentclass will be howto,
#  otherwise chapter will be used.
#
latex_toplevel_sectioning = 'section'

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# If false, will not define \strong, \code, \titleref, \crossref ... but
# only \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'F5_Container_Connectors_doc',
     'F5 Container Connectors Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'F5_Container_Connectors_doc',
     'F5 Container Connectors Documentation',
     author, 'F5 Container Connectors'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'https://docs.python.org/': None}
