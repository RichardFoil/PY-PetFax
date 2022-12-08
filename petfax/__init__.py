#configur
from flask import Flask
#app Factory
def create_app():
    app = Flask(__name__)
    
    #index
    @app.route('/')
    def index():
        return 'Hello, PetFax'

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    #register pet fact
    from . import fact
    app.register_blueprint(fact.bp)
        
    #return the app
    return app