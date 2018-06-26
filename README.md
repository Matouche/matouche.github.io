# Portfolio sources

## Install steps

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install pelican Markdown ghp-import webassets libsass cssmin
$ pelican-themes -s path/to/repository/themes/mportfolio
```

## Usage

```
$ pelican -dr
$ make publish github
```
