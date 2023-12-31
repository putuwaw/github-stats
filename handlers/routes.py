from flask import request, redirect, make_response
from modules import rest, generator, graphql


def configure_routes(app):
    @app.route("/")
    def index():
        return redirect("https://github.com/putuwaw/github-stats/", code=302)

    @app.route("/api")
    def api():
        args = request.args
        username = args.get("username")
        theme = args.get("theme")

        if username is None:
            title = "Error! Username Not Found!"
            message = "Please provide username as a query parameter."
            response = make_response(generator.get_error(title, message))
            response.headers['Content-Type'] = 'image/svg+xml'
            return response
        else:
            try:
                name, repos = rest.get_name_total_repos(username)
                stars, forks = rest.get_total_stars_earned(username, repos)
                pr = rest.get_total_merged_pr(username)
                commits = rest.get_total_commits(username)

                response = make_response(generator.get_svg(
                    name, username, repos, stars, forks, pr, commits, theme))
                response.headers['Content-Type'] = 'image/svg+xml'
                return response

            except BaseException:
                title = "Error! Something Went Wrong!"
                message = "Please check your username or try again later."
                response = make_response(generator.get_error(title, message))
                response.headers['Content-Type'] = 'image/svg+xml'
                return response

    @app.route("/api/graphql")
    def api_graphql():
        args = request.args
        username = args.get("username")
        theme = args.get("theme")

        if username is None:
            title = "Error! Username Not Found!"
            message = "Please provide username as a query parameter."
            response = make_response(generator.get_error(title, message))
            response.headers['Content-Type'] = 'image/svg+xml'
            return response
        else:
            try:
                name, repos = graphql.get_name_total_repos(username)
                stars, forks = graphql.get_total_stars_earned(username)
                pr = graphql.get_total_merged_pr(username)
                commits = graphql.get_total_commits(username)

                response = make_response(generator.get_svg(
                    name, username, repos, stars, forks, pr, commits, theme))
                response.headers['Content-Type'] = 'image/svg+xml'
                return response

            except BaseException:
                title = "Error! Something Went Wrong!"
                message = "Please check your username or try again later."
                response = make_response(generator.get_error(title, message))
                response.headers['Content-Type'] = 'image/svg+xml'
                return response
