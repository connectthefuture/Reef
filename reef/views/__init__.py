from pyramid.view import view_config


@view_config(route_name='reef.index', request_method='GET', renderer='json')
def index(request):
    return {'ok': True}


@view_config(route_name='reef.home', renderer='/reef/index.plim')
def home(request):
    """
    :type request: :class:`pyramid.request.Request`
    """
    users_repo = request.db.get_repository('users')
    user = users_repo.get_by_id(1)
    return {'project': 'Pacific', 'user': user}
