from cleaver.reports.web import CleaverWebUI
from cleaver.backend.db import SQLAlchemyBackend

app = CleaverWebUI(SQLAlchemyBackend('sqlite:///experiment.data'))

from wsgiref import simple_server
print "Serving at 0.0.0.0:8081"
simple_server.make_server('', 8081, app).serve_forever()
