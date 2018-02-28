# Functions in here would really go look at the file /etc/acme_cfg.ini and
# get/set things in there. We're just interested in seeing how the server
# code is structured, so we just use a local dictionary of settings.

configs = {
    'basics': {
        'pi': '3.1416',
        'answer': '42',
        'result': 'okay'
    },
    'places': {
        'ip': '192.168.1.1',
        'country': 'Brazil',
        'domain': 'google.com'
    },
    'corral': {
        'animals': 'pigs cows',
        'max_animals': '10'
    }
}

def get_config_sections():
    # cheat: should really search /etc/acme_cfg.ini for all section names
    return list(configs.keys())

def get_config_section(section_name):
    # cheat: should really read /etc/acme_cfg.ini, section 'section_name',
    # and return settings as a dictionary, or None if section not found
    return configs[section_name]

def get_config_item(section_name, item_name):
    result = configs[section_name][item_name]
    print("get_config_item(%s, %s) -> %s" % (section_name, item_name, result))
    return result

# Status stuff, also read from elsewhere

statuses = {
    'versions': {
        'component-1': 'v1.0',
        'component-2': 'v9.17'
    }
}

def get_status_sections():
    return list(statuses.keys())

def get_status_section(section_name):
    return statuses[section_name]

def get_status_item(section_name, item_name):
    return statuses[section_name][item_name]
