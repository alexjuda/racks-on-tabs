import waitress

from . import app


def main():
    args = app.make_cli_parser().parse_args()
    flask_app = app.make_app(args.csv_path)
    waitress.serve(flask_app, port=args.port)


main()
