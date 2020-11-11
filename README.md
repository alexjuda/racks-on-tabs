# racks-on-tabs

> (What you got?) Racks on tabs on tabs
>
> (He got) Racks on tabs on tabs
>
> (We got) Racks on tabs on taaabs
>
> ~[YC & Future, circa 2011, probably](https://www.youtube.com/watch?v=r5w21_Vphbg&ab_channel=ycvevo)

Command line app for browsing CSV files with row lazy loading.

```sh
$ python -m python -m racks_on_tabs.app <PATH_TO_CSV>
```

Starts a local webserver that serves the app content, accessible at [localhost:5000](http://localhost:5000).

# Installation

(TODO)

## pipx

_racks-on-tabs_ is a Python app with a set of dependencies.
The recommended way to install it is via [pipx](https://github.com/pipxproject/pipx):

```sh
pipx install racks-on-tabs
```

## virtualenv

Alternatively, you can set up a local virtual env and install _racks-on-tabs_ there:

``` sh
python3 -m venv venv
source venv/bin/activate
pip3 install racks-on-tabs
python -m racks_on_tabs.app <PATH_TO_CSV>
```

