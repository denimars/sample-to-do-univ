from app import app

if __name__=='__main__':
    app.run(host='localhost', port='8099', debug=True, threaded=True)