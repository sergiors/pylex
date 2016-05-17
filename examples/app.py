# -*- coding: utf-8 -*-

from pylex import Application
from pylex.providers import HttpProvider, LoggerProvider, JinjaProvider

app = Application()
app.register(LoggerProvider())
app.register(HttpProvider())
app.register(JinjaProvider())


@app.get('/name/<name>')
def hello(name):
    return 'Hello %s' % name

if __name__ == '__main__':
    app.run()
