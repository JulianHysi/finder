"""Use this module to run the application

Run the application only if this module is executed directly.
Set the debug mode on.
"""


from finder import app
 
if __name__ == '__main__':
    app.run(debug=True)
