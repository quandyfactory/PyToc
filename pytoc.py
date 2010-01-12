#!/usr/bin/env python

"""
This code takes an HTML page and generates a table of contents.
"""

__version__ = '0.2'
__releasedate__ = '2010-01-11'
__author__ = 'Ryan McGreal <ryan@quandyfactory.com>'
__homepage__ = 'http://quandyfactory.com/projects/40/pytoc'
__repository__ = 'http://github.com/quandyfactory/PyToc'
__copyright__ = 'Copyright (C) 2010 by Ryan McGreal. Licenced under GPL version 2. http://www.gnu.org/licenses/gpl-2.0.html'


from BeautifulSoup import BeautifulSoup as bs
import re
 
def make_toc(html_in, levels=[3, 4]):
    """
    Takes an HTML page and generates a table of contents.
    headings takes a list of HTML heading levels from 1 to 6,
    and builds the TOC for the specified levels.
    """
    # initialize numbering for sections
    levels.sort()
    numbering = [[level, 0] for level in levels]
 
    # initialize toc list
    toc_list = []
 
    # take a beautifulsoup parse tree of the html
    soup = bs(html_in)
 
    # generate a regex to find headings for the table of contents
    heading_regex = '|'.join([str(level) for level in levels])
    search = re.compile('^h(%s)$' % (heading_regex))
 
    # capture a list of headings we care about
    headings = soup.findAll(search)
 
    # start walking the parse tree
    for heading in headings:
        this_num = int(heading.name[-1])
        for number in numbering:
            if number[0] == this_num:
                numbering[numbering.index(number)][1] += 1
            if number[0] > this_num:
                numbering[numbering.index(number)][1] = 0
 
        # generate toc_anchor
        this_toc_anchor = '.'.join(['%s' % number[1] for number in numbering])
        this_toc_anchor = this_toc_anchor.replace('.0', '')

        # add to contents
        toc_list.append((this_toc_anchor, heading.string))
 
        # update heading with anchor
        heading.find(text=heading.string).replaceWith('<a href="#toc_%s" title="Link directly to section %s">%s</a><a name="toc_%s"></a> <span title="Section %s: %s">%s</span> <a href="#" title="Back to top"> &uarr; </a>' % (this_toc_anchor, this_toc_anchor, this_toc_anchor, this_toc_anchor, this_toc_anchor, heading.string, heading.string))
 
    html_out = str(soup)
    return toc_list, html_out
 
 
def count_chars(string, char):
    """
    Returns an integer of how many times char appears in string
    """
    charcount = 0
    for s in string:
        if s == char:
            charcount += 1
    return charcount


def format_contents(toc_list, levels=[3, 4], id="toc"):
    """
    Takes a toc_list from make_toc() and returns an HTML table of contents
    """
    html = []
    addline = html.append
    addline('<h2><a name="%s">Contents</a></h2>' % id)
    addline('<table id="%s_table">' % id)
    for t in toc_list:
        addline('<tr>')
        dots = count_chars(t[0], '.')
        if dots == 0:
            addline('<td class="%s_section_number">%s</td><td colspan="%s"><a href="#%s_%s">%s</a></td>' % (
                id, t[0], len(levels), id, t[0], t[1])
                )
        else:
            for loop in range(dots):
                addline('<td class="%s_section_number"></a>' % (id))
            addline('<td class="%s_section_number">%s</a>' % (id, t[0]))
            addline('<td colspan="%s"><a href="#%s_%s">%s</a></td>' % (len(levels)-dots, id, t[0], t[1]))
        addline('</tr>')
    addline('</table>')
    html_out = '\n'.join(html)
    return html_out
    
    
