import argparse
import csv

import flask


def _url_for(route_name, **params):
    return flask.url_for(route_name, **params)


def _make_app(csv_path):
    app = flask.Flask(__name__)

    @app.route('/')
    def _index():
        csv_doc = _read_csv_doc(csv_path, 0, -1)
        return flask.render_template('index.html',
                                     csv_path=csv_path,
                                     n_rows=csv_doc['n_all_rows'],
                                     n_cols=len(csv_doc['col_names']),
                                     table_headers=csv_doc['col_names'],
                                     app_js_url=_url_for('static', filename='app.js'))

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
        all_rows = list(reader)

        return {'rows': list(enumerate(all_rows))[after_id + 1:after_id + 1 + n_rows],
                'n_all_rows': len(all_rows),
                'col_names': reader.fieldnames}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path')
    args = parser.parse_args()

    app = _make_app(args.csv_path)
    app.run(debug=True)


if __name__ == '__main__':
    main()
