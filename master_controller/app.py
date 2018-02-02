# -*- coding: utf-8 -*-
"""Example Master Controller."""
import os
import json

from flask import request
from flask_api import FlaskAPI
from pymongo import MongoClient
import pika

APP = FlaskAPI(__name__)
DB = MongoClient(os.getenv('DATABASE_URL')).master_controller
BLOCKS = DB.scheduling_blocks
MQ = pika.BlockingConnection(pika.URLParameters(os.getenv('MQ_URL')))
CHANNEL = MQ.channel()

def block_repr(block):
    """Return representation of a processing block document."""
    return {
        '_id': block['_id'],
        'processing_blocks': block['processing_blocks']
    }

@APP.route('/schedulingblocks', methods=['GET', 'POST'])
def scheduling_block_list():
    """Scheduling block list resource"""
    if request.method == 'POST':
        data = request.get_json(silent=False)
        block_id = 0
        for block in BLOCKS.find({}):
            block_id = max(block_id, int(block['_id'].lstrip('sb-')))
        print('max block_id = ', block_id)
        data['_id'] = 'sb-%02i' % (block_id + 1)
        BLOCKS.insert_one(data)
        CHANNEL.queue_declare(queue='scheduling')
        CHANNEL.basic_publish(exchange='',
                              routing_key='scheduling',
                              body=json.dumps(data))
        return block_repr(data), 202

    return [block_repr(block) for block in BLOCKS.find({})]


@APP.route('/schedulingblock/<block_id>', methods=['GET', 'PUT', 'DELETE'])
def scheduling_block_detail(block_id):
    """Retrieve scheduling block"""
    if request.method == 'PUT':
        return dict(message='Update not implemented'), 501

    elif request.method == 'DELETE':
        result = BLOCKS.delete_one({'_id': block_id})
        CHANNEL.queue_declare(queue='delete')
        CHANNEL.basic_publish(exchange='',
                              routing_key='delete',
                              body=json.dumps({'_id': block_id}))
        if result.deleted_count == 1:
            return dict(message='Deleted block: _id={}'.format(block_id)), 200
        return dict(message='Unable to delete block.'), 400

    block = BLOCKS.find_one({'_id': block_id})
    return block_repr(block)
