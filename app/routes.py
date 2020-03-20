from app import app

@app.route('/', methods=["GET"])
def root():
    return '''
    <h1> Welcome home </h1>
    '''