import os
from telethon import TelegramClient
from datetime import datetime
import asyncio

# TODO refactor 

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
TIME_SLEEP = os.getenv("TIMESLEP")

# TODO Need implementation
class DataBase():
    pass

db = DataBase()

class Log():
    pass 
    def time(self):
        current_time = datetime.now()
        return current_time


class Task():

    @property
    def time(self) -> datetime:
        pass

    @property
    def message(self) -> str:
        pass

    @property
    def img(self) -> str or None:
        pass

    @property 
    def chennel(self) -> str:
        pass
    @staticmethod   
    async def sleep():
        asyncio.sleep(TIME_SLEEP)

class TaskGenerator:
    pass

async def main():
    tasks = TaskGenerator()
    async for task in tasks:
        task.sleep()

