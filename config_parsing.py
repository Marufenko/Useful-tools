import configparser

def return_config(section, key):
    parser = configparser.ConfigParser()
    parser.read('config.ini')

    return parser.get(section, key)

print(return_config('db', 'user_name'))