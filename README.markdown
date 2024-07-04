# PyToc

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

* Version: 0.5

* Release Date: 2024-07-04

## Revision History

### Version: 0.5

* Release Date: 2024-07-04

* Changes:

    * Added features argument to bs function call

### Version: 0.4

* Release Date: 2023-09-07

* Changes:

    * Fixed bug based on differences between Python2 and Python3.

### Version: 0.3

* Release Date: 2010-01-18

* Changes:

    * Converted functions into a class with properties and methods. See "Using PyToc", below.

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
    
### Using PyToc
    
You can see the code in action on my website's [About](http://quandyfactory.com/about/) page.

It's pretty simple to use. [Download](http://github.com/quandyfactory/PyToc) pytoc.py and save it somewhere in your PATH. 

Here's a demonstration:

    import urllib
    import pytoc
    
    url = 'http://quandyfactory.com/projects/40/pytoc'
    page = urllib.urlopen(url)
    html = page.read()

    toc = pytoc.Toc(html_in=html)
    toc.make_toc()
    
    toc.html_toc # returns an HTML table of contents
    toc.html_out # returns the html with anchors and numbering in headings
    toc.toc_list # returns a list of tuples in the form (section number, title)

#### Input Properties

The following are input properties you enter to generate the table of contens.

* html_in - The HTML document for which you want to generate a table of contents.

    This is the only necessary property to assign. The rest have default values that may meet your needs.

* levels - A list of numbers corresponding to the heading levels you want to include in your TOC.

    E.g. [3, 4] would include `<h3>` and `<h4>` headings.

    Default is [3, 4].

* id - The base id of the HTML table of contents to be generated.

    Default is "toc".

* title - The title of the generated table of contents.

    Default is "Contents".

#### Methods

* make_toc() - this generates the table of contents and populates the output properties. 

    Returns True when complete.

#### Output Properties

After calling the make_toc() method, the following output properties are populated with values.

* html_out - The same as html_in except with the TOC anchors and numbering included in the headings.

* html_toc - The generated HTML table of contents.

* toc_list - A list of tuples containing the anchors and headings, in case you would rather roll your own HTML table of contents. 

That's it, really.
