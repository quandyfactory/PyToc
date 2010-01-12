#PyToc

Takes an HTML page and generates a table of contents.

## Author

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Homepage: [http://quandyfactory.com/projects/40/pytoc](http://quandyfactory.com/projects/40/pytoc)
* Repository: [http://github.com/quandyfactory/PyToc](http://github.com/quandyfactory/PyToc)

## Licence

Released under the GNU General Public Licence, Version 2:

[http://www.gnu.org/licenses/old-licenses/gpl-2.0.html](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html)

## This Version

* Version: 0.2

* Release Date: 2010-01-11

## Revision History

### Version: 0.21

* Release Date: 2010-01-11

* Changes:

    * Fixed HTML rendering error in format_contents()
    
    ### Version: 0.2

* Release Date: 2010-01-11

* Changes:

    * Fixed bugs
    * Cleaned up code
    * Added format_contents() to generate an HTML table of contents
    * Added count_chars() for use inside format_contents()
    
### Version: 0.11

* Release Date: 2010-01-11

* Changes:

    * Fixed formatting
    * Added heading permalink
        
### Version: 0.1

* Release Date: 2010-01-11

* Changes:

    * First Commit
    

You can see the code in action on my website's [About](http://quandyfactory.com/about/) page.

It's pretty simple to use. [Download](http://github.com/quandyfactory/PyToc) pytoc.py and save it somewhere in your PATH. 

Here's a demonstration:

    import urllib
    import pytoc
    
    url = 'http://quandyfactory.com/projects/40/pytoc'
    page = urllib.urlopen(url)
    html_in = page.read()

    toc_list, html_out = pytoc.make_toc(html_in, [2, 3, 4])

####Using make_toc()

The function `pytoc.make_toc()` takes two parameters:

1. `html_in` - a string of the HTML on which to generate the table of contents; and
2. `levels` - a list of integers corresponding to the heading levels to be included in the table of contents, e.g. 3 corresponds to `<h3>`. The default value is `[3, 4]`.

This function produces two return values:

1. `toc_list` - a list of tuples containing `(section_number, heading text)` for the table of contents; and
2. `html_out` - the html string, modified to include anchors so the table of contents can link to the sections. 

####Using format_contents()

You can take the list returned by `toc_list` and roll your own HTML table of contents; or you can use the built-in generator, `pytoc.format_contents()`.

    table = pytoc.format_contents(toc_list, [2, 3, 4], "table_of_contents")

This function takes 3 parameters:

1. `toc_list` - this is the list output by `make_toc()`. 
2. `levels` - again, a list of integers corresponding to the heading levels to be included in the table of contents, e.g. 3 corresponds to `<h3>`. The default value is `[3, 4]`.
3. `id` - this is an HTML id attribute, used when generating the table id and td classes. The default value is `toc`.

It returns one value:

1. `html_out` - the HTML table of contents. Yes, it's an HTML `<table>`.

That's pretty much it. You can use the toc_list to roll your own presentation for your table of contents.

