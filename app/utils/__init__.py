class Router:
    def run(app):
        print('**************************router**************')
    

        from weather.routs import weather_api
        app.register_blueprint(weather_api)

        from posts.routs import posts_api
        app.register_blueprint(posts_api)