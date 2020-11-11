import argparse
import csv

import flask


def _url_for(route_name, **params):
    return flask.url_for(route_name, **params)


def _make_app(csv_path):
    app = flask.Flask(__name__)

    @app.route('/')
    def _index():
        csv_doc = _read_csv_doc(csv_path)
        return flask.render_template('index.html',
                                     csv_path=csv_path,
                                     n_rows=len(csv_doc['rows']),
                                     n_cols=len(csv_doc['col_names']),
                                     table_headers=csv_doc['col_names'],
                                     app_js_url=_url_for('static', filename='app.js'))

    @app.route('/partial/rows')
    def _partial_rows():
        csv_doc = _read_csv_doc(csv_path)
        return flask.render_template('table_rows.html',
                                     rows_values=[[row[col]
                                                   for col in csv_doc['col_names']]
                                                  for row in csv_doc['rows']])

    return app


def _read_csv_doc(path):
    with open(path) as f:
        reader = csv.DictReader(f)

        return {'rows': list(reader),
                'col_names': reader.fieldnames}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path')
    args = parser.parse_args()

    app = _make_app(args.csv_path)
    app.run(debug=True)


if __name__ == '__main__':
    main()
