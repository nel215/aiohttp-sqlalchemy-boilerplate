# coding: utf-8
from aiopg.sa import create_engine


class EngineCreater(object):
    async def create(self):
        return create_engine(
            user='user',
            password='pass',
            host='db',
            database='db',
        )
