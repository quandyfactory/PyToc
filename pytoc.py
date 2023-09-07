#!/usr/bin/env python

"""
This code takes an HTML page and generates a table of contents.
"""

__version__ = '0.4'
__releasedate__ = '2023-09-07'
__author__ = 'Ryan McGreal <ryan@quandyfactory.com>'
__homepage__ = 'http://quandyfactory.com/projects/40/pytoc'
__repository__ = 'http://github.com/quandyfactory/PyToc'
__copyright__ = 'Copyright (C) 2010 by Ryan McGreal. Licenced under GPL version 2. http://www.gnu.org/licenses/gpl-2.0.html'


from bs4 import BeautifulSoup as bs
import re

class Toc:
    """
    Takes an HTML page and generates a table of contents.
    
    Input Properties:
        html_in - The HTML document for which you want to generate a table of contents.
        levels - A list of numbers corresponding to the heading levels you want to include in your TOC.
            E.g. [3, 4] would include <h3> and <h4> headings.
            Default is [3, 4].
        id - The base id of the HTML table of contents to be generated.
            Default is "toc".
        title - The title of the generated table of contents.
            Default is "Contents".
    
    Methods:
        make_toc() - this generates the table of contents and populates the output properties. 
            Returns True when complete.
        
    Output Properties:
        html_out - The same as html_in except with the TOC anchors and numbering included in the headings.
        html_toc - The generated HTML table of contents.
        toc_list - The list of anchors and headings if you would rather roll your own HTML table of contents.
    """
    
    def __init__(self, html_in='', levels=[3, 4], id='toc', title='Contents'):
        self.html_in = html_in
        self.levels = levels
        self.id = id
        self.title = title
        self.html_out = '' # the html with anchors and numbering included in headings
        self.toc_list = [] # a list of headings and anchors for the table of contents
        self.html_toc = '' # self.toc_list generated into an HTML table.
        
    def make_toc(self):
        """
       Generates a table of contents from self.html_in.
       """
        self.toc_list = [] # reset toc_list
       
        self.levels.sort() # sort the levels
        
        numbering = [[level, 0] for level in self.levels]

        # take a beautifulsoup parse tree of the html
        soup = bs(self.html_in)
 
        # generate a regex to find headings for the table of contents
        heading_regex = '|'.join([str(level) for level in self.levels])
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
            self.toc_list.append((this_toc_anchor, heading.string))
            
            # update heading with anchor
            heading.find(text=heading.string).replaceWith('<a href="#%s_%s" title="Link directly to section %s">%s</a><a name="%s_%s"></a> <span title="Section %s: %s">%s</span> <a href="#" title="Back to top"> &uarr; </a>' % (self.id, this_toc_anchor, this_toc_anchor, this_toc_anchor, self.id, this_toc_anchor, this_toc_anchor, heading.string, heading.string))
        
        self.html_out = str(soup).replace('&lt;', '<').replace('&gt;', '>').replace('&amp;uarr;', '&uarr;')
        self.html_toc = self.format_contents()

        return
 
    def count_chars(self, string, char):
        """
        Returns an integer of how many times char appears in string
        """
        charcount = 0
        for s in string:
            if s == char:
                charcount += 1
        return charcount

    def format_contents(self):
        """
        Takes a toc_list from make_toc() and returns an HTML table of contents
        """
        html = []
        addline = html.append
        #addline('<h2><a name="%s">%s</a></h2>' % (self.id, self.title))
        addline('<table id="%s_table">' % (self.id))
        addline('<caption>%s</caption>' % (self.title))
        for t in self.toc_list:
            addline('<tr>')
            dots = self.count_chars(t[0], '.')
            if dots == 0:
                addline('<td class="%s_section_number">%s</td><td colspan="%s"><a href="#%s_%s">%s</a></td>' % (
                    self.id, t[0], len(self.levels), self.id, t[0], t[1])
                    )
            else:
                for loop in range(dots):
                    addline('<td class="%s_section_number"></td>' % (self.id))
                addline('<td class="%s_section_number">%s</td>' % (self.id, t[0]))
                addline('<td colspan="%s"><a href="#%s_%s">%s</a></td>' % (len(self.levels)-dots, self.id, t[0], t[1]))
            addline('</tr>')
        addline('</table>')
        return ''.join(html)
        
    
