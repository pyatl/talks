import time
import responder

api = responder.API()


# Returning JSON?  Just return a dict!
@api.route("/hello/{who}/json")
def hello_to(req, resp, *, who):
    resp.media = {"hello": who}


@api.route("/hello/{who}/html")
def hello_html(req, resp, *, who):
    resp.html = api.template('template.html', who=who)


@api.route("/teapot")
def teapot(req, resp):
    resp.status_code = api.status_codes.HTTP_416   # ...or 416


@api.route("/pizza")
def pizza_pizza(req, resp):
    resp.headers['X-Pizza'] = '42'


@api.route("/incoming")
async def receive_incoming(req, resp):

    @api.background.task
    def process_data(data):
        """Just sleeps for three seconds, as a demo."""
        print('Doing background stuff')
        time.sleep(1)
        print('Doing more background stuff...')
        time.sleep(1)
        print('Almost done...')
        time.sleep(1)
        print('Done!')

    # Parse the incoming data as form-encoded.
    # Note: 'json' and 'yaml' formats are also automatically supported.
    data = await req.media()

    # Process the data (in the background).
    process_data(data)

    # Immediately respond that upload was successful.
    resp.media = {'success': True}


if __name__ == '__main__':
    api.run()
