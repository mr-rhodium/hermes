import os
from telethon import TelegramClient
from datetime import datetime
import asyncio
from dotenv import dotenv_values
from telethon.tl.functions.channels import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

config = dotenv_values(".env")
print(config)

# TODO refactor

api_id = config.get("API_ID")
print(api_id, "APIID")
api_hash = config.get("API_HASH")
TIME_SLEEP = os.getenv("TIMESLEP")


# TODO Need implementation
class DataBase:
    pass


db = DataBase()


class Log:
    pass

    def time(self):
        current_time = datetime.now()
        return current_time


class Task:
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


# async def main():
#     tasks = TaskGenerator()
#     async for task in tasks:
#         task.sleep()

session = "1ApWapzMBu3KFCNI4SmDRnBDelHEAKhhS8l7FhTYgHLTcwxY_AYANa3Ut4-6890WhbNOHuKksHiyR_0N_Pm_3BBna9TNF1oxjoiDdv_VvmWhiQedSWMYKnp0K1HLM77RdnKnK0leXuXJIyaBdo5eiTEmr40Gj7aM3q-Pw6ujK_mUjQKViZ9gBkjCiT6MD3xf7Bj8LfK-0TSWSmUgoE9pb9XMnzvFk4bpz76AMKNGUkVm91kdtC8xkO09ZAfgXjAAatal1ArRQCxtChiTreyrFos6f9Ic4-p4JikadcTvsnpTds_rTLOSdQDVqq8wGDtX-v6c5vFGnt7PTat1dAAM80bk5235PAu8="

with TelegramClient("session=session", api_hash=api_id, api_id=api_id) as client:
    result = client(
        GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=500,
            hash=0,
        )
    )

    for chat in result.chats:
        print(chat)
