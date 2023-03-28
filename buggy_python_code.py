import urllib3
import yaml
import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    """
    Flask index
    :return:
    """
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}


class Person(object):
    """
    Describing the person
    """
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    """
    Printing nametag
    :param format_string: format string
    :param person: person name
    :return:
    """
    print(format_string.format(person=person))


def fetch_website(urllib_version_fun, url) -> None:
    """
    Fetching the website
    :param urllib_version_fun: version
    :param url: url
    :return: None
    """
    # Import the requested version (2 or 3) of urllib
    exec(f"import urllib{urllib_version_fun} as urllib", globals())
    # Fetch and print the requested URL

    http = urllib3.PoolManager()
    request_our = http.request('GET', url)

    print(request_our)


def load_yaml(filename) -> dict:
    """
    Loading yaml
    :param filename: filename
    :return: dictionary with deserialized data
    """
    with open(filename, "r") as stream:
        # deserializing data
        deserialized_data = yaml.load(stream, Loader=yaml.Loader)

    return deserialized_data


def authenticate(actual_password) -> None:
    """
    Function which authenticates user
    :param actual_password: Your password
    :return: None
    """
    # Assert that the password is correct
    assert actual_password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability: use string={person.__init__.__globals__[CONFIG][API_KEY]}")
    print("2. Code injection vulnerability: use string=;print('Own code executed') #")
    print("3. Yaml deserialization vulnerability: use string=file.yaml")
    print("4. Use of assert statements vulnerability: run program with -O argument")
    choice = input("Select vulnerability: ")
    if choice == "1": 
        new_person = Person("Vickie")  
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urllib_version = input("Choose version of urllib: ")
        fetch_website(urllib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)
