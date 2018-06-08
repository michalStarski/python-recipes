from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static')
    config.add_route('home', '/')
    config.add_route('form', '/recipe/new')
    config.add_route('new', '/recipe/api/new')
    config.add_route('recipe', '/recipe/{id}')
    config.scan()
    return config.make_wsgi_app()
