# -*- coding: utf-8 -*-
"""Initialise the Master Controller database."""
import os

from pymongo import MongoClient


def init_db():
    """Initialse the database."""
    blocks = [
        {
            '_id': 'sb-01',
            'processing_blocks': [
                {
                    'id': 'pb-01',
                    'config': {}
                },
                {
                    'id': 'pb-02',
                    'config': {}
                }
            ]
        },
        {
            '_id': 'sb-02',
            'processing_blocks': [
                {
                    'id': 'pb-03',
                    'config': {}
                },
                {
                    'id': 'pb-04',
                    'config': {}
                }
            ]
        },
    ]

    db = MongoClient(os.getenv('DATABASE_URL')).master_controller
    sched_blocks = db.scheduling_blocks
    sched_blocks.delete_many({})
    sched_blocks.insert_many(blocks, ordered=True)
    sched_blocks = db.scheduling_blocks
    blocks = sched_blocks.find({})
    for block in blocks:
        print(block)


if __name__ == '__main__':
    init_db()
