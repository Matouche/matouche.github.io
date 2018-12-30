python3 -m venv venv
source venv/bin/activate
pip3 install pelican Markdown ghp-import webassets libsass cssmin
pelican-themes -s $(pwd)/themes/mportfolio
deactivate
