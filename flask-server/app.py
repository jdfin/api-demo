import flask
import system
import acme

app = flask.Flask(__name__)

@app.route('/')
def home():
    if flask.request.user_agent.browser:
        # in the webapp version, this is the only page the browser ever loads
        return flask.render_template('index.html')
    else:
        return flask.redirect(flask.url_for('api'))

# api

@app.route('/api')
def api():
    return flask.Response(flask.json.dumps(['config', 'status', 'command']), mimetype='application/json')

@app.route('/api/config')
def api_config():
    return flask.Response(flask.json.dumps(['system', 'acme']), mimetype='application/json')

@app.route('/api/config/acme')
def api_config_acme():
    return flask.Response(flask.json.dumps(acme.get_config_sections()), mimetype='application/json')

@app.route('/api/config/acme/<section_name>')
def api_config_acme_section(section_name):
    try:
        return flask.Response(flask.json.dumps(acme.get_config_section(section_name)), mimetype='application/json')
    except KeyError:
        flask.abort(404)

@app.route('/api/config/system')
def api_config_system():
    return flask.Response(flask.json.dumps(system.get_config_sections()), mimetype='application/json')

@app.route('/api/config/system/<section_name>')
def api_config_system_section(section_name):
    try:
        return flask.Response(flask.json.dumps(system.get_config_section(section_name)), mimetype='application/json')
    except KeyError:
        flask.abort(404)

@app.route('/api/status')
def api_status():
    return flask.Response(flask.json.dumps(['system', 'acme']), mimetype='application/json')

@app.route('/api/status/acme')
def api_status_acme():
    return flask.Response(flask.json.dumps(acme.get_status_sections()), mimetype='application/json')

@app.route('/api/status/acme/<section_name>')
def api_status_acme_section(section_name):
    try:
        return flask.Response(flask.json.dumps(acme.get_status_section(section_name)), mimetype='application/json')
    except KeyError:
        flask.abort(404)

@app.route('/api/status/system')
def api_status_system():
    return flask.Response(flask.json.dumps(system.get_status_sections()), mimetype='application/json')

@app.route('/api/status/system/<section_name>')
def api_status_system_section(section_name):
    try:
        return flask.Response(flask.json.dumps(system.get_status_section(section_name)), mimetype='application/json')
    except KeyError:
        flask.abort(404)

@app.route('/api/command')
def api_command():
    return flask.Response(flask.json.dumps([]), mimetype='application/json')

# browser, only when not using the webapp

# avoid "template not found" exception, return 404 instead
@app.route('/favicon.ico')
def favicon():
    flask.abort(404)

# avoid "template not found" exception, return 404 instead
@app.route('/command.html')
def command():
    flask.abort(404)

@app.route('/<path:path_name>')
def static_page(path_name):
    return flask.render_template(path_name)

@app.route('/config/system/network.html')
def config_system_network():
    return flask.render_template('config/system/network.html',
                                 ip=system.get_config_item('network', 'ip'),
                                 mask=system.get_config_item('network', 'mask'))

@app.route('/config/acme/basics.html')
def config_acme_basics():
    return flask.render_template('config/acme/basics.html',
                                 answer=acme.get_config_item('basics', 'answer'),
                                 pi=acme.get_config_item('basics', 'pi'),
                                 result=acme.get_config_item('basics', 'result'))

@app.route('/config/acme/places.html')
def config_acme_places():
    return flask.render_template('config/acme/places.html',
                                 country=acme.get_config_item('places', 'country'),
                                 domain=acme.get_config_item('places', 'domain'),
                                 ip=acme.get_config_item('places', 'ip'))

@app.route('/config/acme/corral.html')
def config_acme_corral():
    return flask.render_template('config/acme/corral.html',
                                 animals=acme.get_config_item('corral', 'animals'),
                                 max_animals=acme.get_config_item('corral', 'max_animals'))

@app.route('/status/system/versions.html')
def status_system_versions():
    return flask.render_template('status/system/versions.html',
                                 kernel=system.get_status_item('versions', 'kernel'),
                                 build=system.get_status_item('versions', 'build'))

@app.route('/status/acme/versions.html')
def status_acme_versions():
    return flask.render_template('status/acme/versions.html',
                                 component1=acme.get_status_item('versions', 'component-1'),
                                 component2=acme.get_status_item('versions', 'component-2'))
