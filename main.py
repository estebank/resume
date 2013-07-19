#!/usr/bin/env python

__author__ = 'esteban@kuber.com.ar'

import webapp2
from webapp2_extras import routes


### URL MAPPING

protocol = 'http://'
subdomain_esteban = 'esteban.kuber.com.ar'

def redirect(path, target=protocol+subdomain_esteban+'/resume/'):
    return webapp2.Route(path, handler=webapp2.RedirectHandler,
                         defaults={'_uri': lambda request, *args, **kwargs: target})


app = webapp2.WSGIApplication(routes=[
        redirect('/.*', 'http://esteban.kuber.com.ar'),
        routes.DomainRoute(subdomain_esteban, [
            redirect('/resume'),
            redirect('/cv/'),
            redirect('/'),
        ]),
    ],
    debug=False)
