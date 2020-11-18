import argparse
import csv
import itertools as itt

import flask


def _url_for(route_name, **params):
    return flask.url_for(route_name, **params)


def make_app(csv_path):
    app = flask.Flask(__name__)

    @app.route('/')
    def _index():
        csv_doc = _read_csv_doc(csv_path, 0, -1)
        return flask.render_template('index.html',
                                     csv_path=csv_path,
                                     n_cols=len(csv_doc['col_names']),
                                     table_headers=csv_doc['col_names'],
                                     app_css_url=_url_for('static', filename='app.css'),
                                     app_js_url=_url_for('static', filename='app.js'),
                                     favicon_url=_url_for('static', filename='favicon.png'))

    @app.route('/partial/rows')
    def _partial_rows():
        n_rows = int(flask.request.args.get('n_rows', 10))
        after_id = int(flask.request.args.get('after_id', -1))
        csv_doc = _read_csv_doc(csv_path, n_rows, after_id)
        return flask.render_template('table_rows.html',
                                     rows_values=[(row_id, [row[col]
                                                            for col in csv_doc['col_names']])
                                                  for row_id, row in csv_doc['rows']])

    return app


def _read_csv_doc(path, n_rows, after_id):
    with open(path) as f:
        reader = csv.DictReader(f)
        col_names = reader.fieldnames
        rows = [(e_i + after_id + 1, e)
                for e_i, e in enumerate(itt.islice(reader, after_id+1, after_id+1+n_rows))]

        return {'rows': rows,
                'col_names': col_names}


def make_cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path')
    parser.add_argument('-p', '--port',
                        help='HTTP port to serve on. Defaults to 7482',
                        type=int,
                        default=7482)
    return parser


def main():
    args = make_cli_parser().parse_args()
    app = make_app(args.csv_path)
    app.run(port=args.port, debug=True)


if __name__ == '__main__':
    main()
