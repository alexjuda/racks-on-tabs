import argparse

import flask


def _make_app(csv_path):
    app = flask.Flask(__name__)

    @app.route('/')
    def _index():
        return flask.render_template('index.html')

    return app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path')
    args = parser.parse_args()

    app = _make_app(args.csv_path)
    app.run()


if __name__ == '__main__':
    main()
