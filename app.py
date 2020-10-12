from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')  # this is an endpoint route.
def home():
    """
    this function will be called for the home page
    The flask endpoint can NOT return dictionaries.
    That's why we need to import jsonify module
    which can convert the dict into string
    """
    return jsonify({'message': 'Hello!'})


#  This condition is needed to prevent this file from running,
#  when other modules need to access something from this module.
#  When this file is imported we do not run the app.
if __name__ == '__main__':
    app.run()
