from BeautifulSoup import BeautifulSoup as bs
import re
 
def make_toc(html, levels=[3, 4]):
    """
Takes an HTML page and generates a table of contents.
headings takes a list of HTML heading levels from 1 to 6,
and builds the TOC for the specified levels.
"""
    # initialize numbering for sections
    levels.sort()
    numbering = [[level, 0] for level in levels]
 
    # initialize toc list
    toc = []
 
    # take a beautifulsoup parse tree of the html
    soup = bs(html)
 
    # generate a regex to find headings for the table of contents
    heading_regex = '|'.join([str(l) for l in levels])
    search = re.compile('^h(%s)$' % (heading_regex))
 
    # capture a list of headings we care about
    headings = soup.findAll(search)
 
    # start walking the parse tree
    for heading in headings:
        this_num = int(heading.name[-1])
        for number in numbering:
            if number[0] == this_num:
                numbering[numbering.index(number)][1] += 1
            elif number[0] > this_num:
                numbering[numbering.index(number)][1] = 0
 
        # generate toc_anchor
        this_toc_anchor = '.'.join(['%s' % number[1] for number in numbering])
 
        # add to contents
        toc.append((this_toc_anchor, heading.text))
 
        # update heading with anchor
        heading.find(text=heading.text).replaceWith('<a name="toc_%s">%s %s</a>' % (
            this_toc_anchor, this_toc_anchor, heading.text)
            )
 
    return toc, str(soup)
 
