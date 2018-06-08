from pyramid.view import view_config
import json
import pyramid.httpexceptions as exc


@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    return {
        'recipeNumber': '0',
        'figcaption': 'test food',
        }
        
@view_config(route_name='form', renderer='templates/form.jinja2')
def test_view(request):
    return {}


@view_config(route_name='new', renderer='json', request_method='POST')
def createRecipe(request):
    with open('recepies/db.json') as f:
        data = json.load(f)
    data["dishes"].append(request.json_body)
    id = len(data["dishes"])
    with open('recepies/db.json', 'w') as outfile:
        json.dump(data, outfile)
    return {"id": id-1}

@view_config(route_name='new', renderer='json', request_method='OPTIONS')
def foo(request):
    request.response.headers = {"Access-Control-Allow-Origin": "*"}
    return {}


@view_config(route_name='recipe', renderer='templates/recipe.jinja2')
def loadRecipe(request):
    with open('recepies/db.json') as f:
        data = json.load(f)
    dishes = data["dishes"]
    try:    
        id = request.matchdict["id"]
        return {
        "ingredients": dishes[int(id)]["ingredients"],
        "steps": dishes[int(id)]["steps"],
        "image": dishes[int(id)]["photo"],
        "figcaption": dishes[int(id)]["name"],
        "recipeNumber": id
        }
    except:
        raise exc.exception_response(404)