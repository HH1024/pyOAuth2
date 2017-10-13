import tornado.ioloop
import tornado.web
import settings

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, worldr")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], **settings.config)
    application.listen(9999)
    tornado.ioloop.IOLoop.current().start()