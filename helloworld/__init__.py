from flask import abort, render_template, request, current_app, Flask

from config import config

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  @app.route('/')
  def index():
      return render_template('index.html')

  @app.route('/shutdown')
  def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'

  return app


app = create_app('default')
