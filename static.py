#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import webapp2


# Needed to have subdomain-specific static urls
class StaticHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(open(os.path.join(os.path.dirname(__file__), self.path)).read())
