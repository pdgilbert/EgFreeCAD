# EgFreeCAD
FreeCAD scripting examples with testing.
[![Build Status](https://travis-ci.org/pdgilbert/EgFreeCAD.svg?branch=master)](https://travis-ci.org/pdgilbert/EgFreeCAD)

(This is README.md from master branch.)

The 
<a href="https://pdgilbert.github.io/EgFreeCAD/index.html">web pages view</a>
of the results from running these examples will be what most people what to see.

The central part of EgFreeCAD is a Sphinx document with FreeCAD examples and a
python library used to test that two objects created in FreeCAD are
equivalent. Equivalent here means they define the same shape in space.
(Techically, consider A and B are equivalent if both A - B and B - A are empty.)
This provides a mechanism for testing examples.

The document presents many examples, and tests them to be sure they actually work.
The Travis / Github combination implemented here attempts to build the Sphinx
document in different versions of FreeCAD and Python, 
then presents the documents  successfully built in these different
environments. The build will fail if the examples fail.

##  Notes on the Travis work flow
(See also the 
[gh-pages branch *README.md* file](https://github.com/pdgilbert/EgFreeCAD/tree/gh-pages/README.md)
for notes on the Github Pages setup.)

Details of the travis work flow can be seen in the *travis.yml* file. 
A Summary of issues is explained here for anyone who might be trying to 
implement a similar setup (and to remind myself how it works).
And, of course, suggestions for simplifications and improvements are appreciated.

Syntax and examples of *travis.yml* are explained elsewhere much better than I 
can do, so I will point out only my main stumbling blocks:

-Travis `deploy` clears the *gh-pages* branch, which means that different jobs in
the matrix build will clobber each other's results. I had to abandon deploy and
use `after_success`. The `deploy` also clobbered top level *README.md* and 
*index.html* files.

-In the Travis `after_success` I checkout branch *gh-pages* and copy the new build to 
that branch. There seems to remain some danger that different jobs will 
overlap in a way that requires a merge. I have not run into that yet. The merge
should not be difficult because the builds are in directories with different names,
but the script may not handle the possibility that a merge is needed.

-The travis build checkout uses a commit number, so is headless. That presents
a problem if attempting to commit to the *master* branch as I tried to do once.
Checkout of *gh-pages*  and copying the build to that branch avoids this problem.

-It seems a bit diffucult to insure Python 3 uses Sphinx in Python 3 and FreeCAD
in  Python 3. Careful checks neet to be used to guarantee that thinks happened
as intended (see script *freecadPythonCheck*) and throw errors if not.

##  Notes related to work flow , but not really Travis specific

-The PPA for FreeCAD seems to be out of date. Their newer approach may be to use
AppImage, but to run under Sphinx I need to open python and inport freecad. 
I have not figured out how to do that with a AppImage. Also not sure if using
pip or conda may be better here.

It is possible to link to Sphinx build pages with absolute links from
this *README.md* file, for example, 
[go to the FreeCAD/Python 2.7 build.](https://pdgilbert.github.io/EgFreeCAD/build_freecad/Python-2.7/html)


