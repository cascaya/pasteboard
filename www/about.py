#!/usr/bin/env python
"""
    about page 
    first entry point of about page
    @author Anja Siek <anja.marita@web.de>
"""

import cgi, sys
from lib import *
import json

# get cookie
cookie = cookie.Cookie()
c = cookie.get("tk")


if c and not c == "None":
    #if is logged in use different templates
    pages = {'header': 'headerloggedin','footer':'footer','content':'about'}
else:
    pages = {'header': 'header','footer':'footer','content':'about'}

# get layout
template = "layout.html.tpl"
tpl = "".join(open(template,'r').readlines())

# print header
basics.print_headers({'Content-type':'text/html'})
# print page including pages variable
sys.stdout.write(tpl.format(str(json.dumps(pages))))
