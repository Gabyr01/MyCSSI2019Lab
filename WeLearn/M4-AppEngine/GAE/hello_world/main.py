import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['content-Type'] = 'text/plain'
        self.response.write('Hello, World')

class SecretPage(webapp2.RequestHandler):
    def get(self)
        self.response.headers['content-Type'] = 'html'
        self.response.write('<h1>')
        
app = webapp2.WSGIApplication([
    ('/', MainPage)
    ('/secret', SecretPage),
], debug=True)
