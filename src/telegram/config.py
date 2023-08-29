from dataclasses import dataclass
from dynaconf import Dynaconf


@dataclass(frozen=True)
class _TgBotConfig:
    token: str
    skip_updates: bool


@dataclass(frozen=True)
class _AdminIdsConfig:
    ids: list


@dataclass(frozen=True)
class _PostgreSQLConfig:
    host: str
    port: int
    database: str
    user: str
    password: str


@dataclass(frozen=True)
class _RedisConfig:
    host: str
    port: int
    database: int
    password: str


@dataclass(frozen=True)
class Config:
    tgbot: _TgBotConfig
    admin: _AdminIdsConfig
    psql: _PostgreSQLConfig
    redis: _RedisConfig


dynaconf = Dynaconf(settings_files=['configs/config.toml'])
cfg = dynaconf.as_dict()

config = Config(
    tgbot=_TgBotConfig(
        token = cfg['TOKEN'],
        skip_updates=cfg['SKIP_UPDATES']
    ),
    admin=_AdminIdsConfig(
        ids=cfg['ADMIN_IDS']
    ),
    psql=_PostgreSQLConfig(
        host=cfg['PSQL_HOST'],
        port=cfg['PSQL_PORT'],
        database=cfg['PSQL_DATABASE'],
        user=cfg['PSQL_USER'],
        password=cfg['PSQL_PASSWORD']
    ),
    redis=_RedisConfig(
        host=cfg['REDIS_HOST'],
        port=cfg['REDIS_PORT'],
        database=cfg['REDIS_DATABASE'],
        password=cfg['REDIS_PASSWORD']
    )
)