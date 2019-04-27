# EgFreeCAD
FreeCAD scripting examples with testing.

(This is a work in progress.)<P>

Most people will want to look at the results produced by the builds,
which are at the
<a href="https://pdgilbert.github.io/EgFreeCAD/index.html">EgFreeCAD Page</a>.

The source code for these documents and examples is maintained on github at
<a href="https://github.com/pdgilbert/EgFreeCAD/">EgFreeCAD</a>.

##  Notes on this Github Pages setup

(See also the 
[master branch *README.md* file](https://github.com/pdgilbert/EgFreeCAD/README.md)
for notes on the Travis work flow.)

The notes here are mainly for anyone who might be trying to implement 
a similar setup. (And to remind myself how it works.)

Editing gh-pages branch pages, such as this *README.md* file and 
the *index.html* file,  in normal git fashion will require some 
attention to the fact that builds are pushing to the gh-pages branch. 
Be sure to fetch/pull before editing, then edit/commit/push when builds 
are not being done or you will have to do more 
complicate merges when you push.

The main trick in getting the Sphinx output with its CSS to display properly
on GitHub Pages is to disable Jekyll processing by having a file *.nojekyll*
in the web site top level directory (no file contents necessary).
This trick does not seem to work if the *.nojekyll* is down in the html 
directory generated by the build. (It is suggested some places that that will
work, and it may if the html/ is the top level, but I had no luck.)

An additional result 
of the <i>.nojekyll</i> file is that the <i>README.md</i> file does not
get processed into an <i>index.html</i> file for the website top level. 
So an <i>index.html</i> file is needed.
 
I have so far had no luck listng files in a directory, which would be useful
for looking at doctest results.

It is possible to link to Sphinx build pages with absolute links from
this *README.md* file, for example, 
[go to the FreeCAD/Python 2.7 build.](https://pdgilbert.github.io/EgFreeCAD/build_freecad/Python-2.7/html)

