import argparse
import csv

import flask


def _make_app(csv_path):
    app = flask.Flask(__name__)

    @app.route('/')
    def _index():
        rows = _read_csv(csv_path)
        return flask.render_template('index.html',
                                     n_rows=len(rows),
                                     n_cols=len(rows[0].keys()),
                                     rows=rows)

    return app


def _read_csv(path):
    with open(path) as f:
        return [row
                for row in csv.DictReader(f)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path')
    args = parser.parse_args()

    app = _make_app(args.csv_path)
    app.run()


if __name__ == '__main__':
    main()
