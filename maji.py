#!/usr/bin/env python3
"""maji.

Usage:
  maji <template>
"""
import os
from sys import stdin

from docopt import docopt

from jinja2 import Environment
from jinja2 import FileSystemLoader

import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)


def jinja(template, templates, **context):
    templates = os.path.abspath(templates)
    env = Environment(loader=FileSystemLoader((templates,)))
    template = env.get_template(template)
    out = template.render(**context)
    return out


def main():
    arguments = docopt(__doc__, version='maji 0.1')
    # render markdown to html
    content = markdown(stdin.read())
    # render template with `content`
    template = arguments['<template>']
    templates = os.path.abspath(template)
    templates = os.path.dirname(templates)
    out = jinja(template, templates, content=content)
    print(out)
