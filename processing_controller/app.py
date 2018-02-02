# -*- coding: utf-8 -*-
"""Example service with subscribing to a MQ.

TODO:
- [ ] Callbacks should be non blocking - use Celery?
- [ ] This should interact with a Processing Controller Db.
- [ ] An API serice should provide a REST API in front of the PC
"""
import json
import pika


def new_scheduling_block_request(ch, method, properties, body):
    """Callback."""
    print(" + Received new block request:")
    print(json.dumps(json.loads(body), indent=2, sort_keys=True))


def rem_scheduling_block_request(ch, method, properties, body):
    """Callback."""
    print(" - Received block remove request:")
    print(json.dumps(json.loads(body), sort_keys=2))


def main():
    """Main function"""
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare('scheduling')
        channel.queue_declare('delete')
        channel.basic_consume(new_scheduling_block_request,
                              queue='scheduling',
                              no_ack=True)
        channel.basic_consume(rem_scheduling_block_request,
                              queue='delete',
                              no_ack=True)
        print('Waiting for messages. CTRL+C to exit.')
        channel.start_consuming()
    except pika.exceptions.ConnectionClosed as error:
        print(error)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
