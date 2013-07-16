#!/usr/bin/env python

__author__ = 'esteban@kuber.com.ar'

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template
import os
import webapp2
from webapp2_extras import routes


def render(template_file, variables=None, template_dir='templates'):
  if variables is None:
    variables = {}
  path = os.path.join(os.path.dirname(__file__), template_dir, template_file)
  return template.render(path, variables)


class CvHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write(render('resume.html', template_dir='resume'))


### URL MAPPING

protocol = 'http://'
subdomain_esteban = 'esteban.kuber.com.ar'

def redirect(path, target=protocol+subdomain_esteban+'/resume/'):
    return webapp2.Route(path, handler=webapp2.RedirectHandler,
                         defaults={'_uri': lambda request, *args, **kwargs: target})


app = webapp2.WSGIApplication(routes=[
        redirect('/.*', 'http://esteban.kuber.com.ar'),
        routes.DomainRoute(subdomain_esteban, [
            webapp2.Route('/resume/', handler=CvHandler, name='resume'),
            redirect('/resume'),
            redirect('/cv/'),
            redirect('/'),
        ]),
        webapp2.Route( r'/google5ddcdcec3c24d2d5.html',
            lambda request, *args, **kwargs: webapp2.Response(
                'google-site-verification: google5ddcdcec3c24d2d5.html')),
    ],
    debug=True)
