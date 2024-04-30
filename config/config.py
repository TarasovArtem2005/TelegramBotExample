from environs import Env
from dataclasses import dataclass


@dataclass
class tg_bot:
    token: str


@dataclass
class Config:
    tg_bot: tg_bot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=tg_bot(bot_tocken=env('BOT_TOCKEN')))
