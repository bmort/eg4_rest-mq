# -*- coding: utf-8 -*-
"""Example service with subscribing to a MQ.

TODO
- [ ] Work out how to combine a MQ with a Flask app. eg.
        https://blog.miguelgrinberg.com/post/using-celery-with-flask
        https://github.com/eandersson/python-rabbitmq-examples/blob/master/Flask-examples/pika_async_rpc_example.py
        https://www.queryoverflow.gdn/query/flask-rabbitmq-socketio-forwarding-messages-27_29461028.html
        http://brunorocha.org/python/microservices-with-python-rabbitmq-and-nameko.html
- [ ] Add endpoint to query for list of current blocks
- [ ] Add endpoint to query for block info
- [ ] Save scheduling block requests to a database
- [ ] Randomly update the a field in the block
- [ ] Subscribe to delete events
- [ ] Connect endpoints to MC
"""
