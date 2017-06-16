from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    """
    Renders the search homepage.
    """
    return render_template("index.html")


@app.route('/search', methods=['GET'])
def search(query=None, searchType=None):
    """
    Returns search results based on query method chosen.

    Parameters:
    {
        query: string,
        searchType: { EN | SUM | AKK | SIGN },
        eng: {
            include: string,
            exclude: string
        },
        sum: {
            containsSign: [ string, ... ],
            containsDet: [ string, ... ],
            startsWith: string,
            endsWith: string,
            enableHomophones: bool
        }
    }
    """
    # parse/clean up query
    # construct db query
    # search with query
    # return results in webpage
    return render_template("search.html")


@app.route('/signsearch')
def signsearch(query=None):
    """
    Returns sign search results on righthand pane of main site.

    Parameters:
    {
        query: string,
        startsWith: string,
        endsWith: string,
        contained: string,
        times: string,
        gunu: bool,
        sessig: bool,
        enableHomophones: bool
    }
    """
    # parse/clean up query
    # construct db query
    # search with query
    # return JSON result
    pass


@app.route('/sign/<id>')
def get_sign(id=None):
    if id is None:
        return "Error: must specify id"
    return render_template("sign.html")


@app.route('/entry/<id>')
def get_entry(id=None):
    if id is None:
        return "Error: must specify id"
    return render_template("entry.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
