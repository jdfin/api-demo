
statuses = {
    'versions': {
        'build': 'v0.1',
        'kernel': '4.4.0-112-generic'
    }
}

def get_status_sections():
    return list(statuses.keys())

def get_status_section(section_name):
    return statuses[section_name]

def get_status_item(section_name, item_name):
    return statuses[section_name][item_name]

configs = {
    'network': {
        'ip': '192.168.1.100',
        'mask': '255.255.255.0'
    },
    'mode': {
        'debug': 'yes',
        'options': 'sluggish'
    }
}

def get_config_sections():
    return list(configs.keys())

def get_config_section(section_name):
    return configs[section_name]

def get_config_item(section_name, item_name):
    return configs[section_name][item_name]
