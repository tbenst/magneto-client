import yaml

PATH = None
MAGNETO = None

class ModuleDictionary:
    """a class for loading and saving a module's dictionary. module is a string,
    like 'core\\copypaste'"""
    def __init__(self,module):
        self.module = module
        self.dictionary = load_dictionary(self.module)

    def __getitem__(self, arg):
        return self.dictionary[arg]

    def __setitem__(self,key,value):
        self.dictionary[key] = value
        self.save()
    
    def save(self):
        save_dictionary(self.module, self.dictionary)



def set_path(path):
    global MAGNETO
    global PATH
    PATH = path
    with open(path + 'etc/magneto.yaml', 'r') as f:
        MAGNETO = yaml.load(f)
    return MAGNETO

def get_path(module, file="settings"):
    global PATH
    if module == 'magneto':
        path = PATH + 'etc\\magneto.yaml'
    elif module == 'enabled':
        path = PATH + 'etc\\enabled.yaml'
    elif file == "settings":
        path = PATH + 'etc\\settings\\' + module + '.yaml'
    elif file == "dictionary":
        path = PATH + 'etc\\dictionaries\\' + module + '.yaml'
    else:
        print("invalid parameters for get_path: %s %s" % (module, file))

    return path

def save(module, obj):
    path = get_path(module)
    with open(path, 'w') as f:
        f.write(yaml.dump(obj, default_flow_style=False))

def save_dictionary(module, obj):
    path = get_path(module, "dictionary")
    with open(path, 'w') as f:
        f.write(yaml.dump(obj, default_flow_style=False))


def load_dictionary(module):
    path = get_path(module, "dictionary")

    try:  
        with open(path, 'r') as f:
            my_setting = yaml.load(f)
    except IOError:
        my_setting = {}
        save_dictionary(module,my_setting)
    return my_setting



def load(module):
    path = get_path(module)
    
    try:
        with open(path, 'r') as f:
            my_setting = yaml.load(f)
    except IOError:
        my_setting = {}
        save(module,my_setting)


    print("setting for module %s" % module, my_setting)
    return my_setting
