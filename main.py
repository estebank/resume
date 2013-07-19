#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import webapp2
from webapp2_extras import routes
from resume.resume import EstebanResume
from javier.cv import JavierCv

### URL MAPPING

protocol = 'http://'
subdomain_esteban = 'esteban.kuber.com.ar'
subdomain_javier = 'esteban.kuber.com.ar'

def redirect(path, target=protocol+subdomain_esteban+'/resume/'):
    return webapp2.Route(path, handler=webapp2.RedirectHandler,
                         defaults={'_uri': lambda request, *args, **kwargs: target})


app = webapp2.WSGIApplication(routes=[
        redirect('/.*', 'http://esteban.kuber.com.ar'),
        routes.DomainRoute(subdomain_esteban, [
            webapp2.Route('/resume/', handler=EstebanResume, name='resume'),
            redirect('/resume'),
            redirect('/résumé/'),
            redirect('/résumé'),
            redirect('/cv/'),
            redirect('/'),
        ]),
        routes.DomainRoute(subdomain_javier, [
            webapp2.Route('/', handler=JavierCv),
            redirect('/.*', protocol+subdomain_javier+'/'),
        ]),
    ],
    debug=False)
