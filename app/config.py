import os
from pathlib import Path

import toml
from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict, SecretStr


class ConfigSection(BaseModel):
    model_config = ConfigDict(extra="ignore")


class BotConfig(ConfigSection):
    token: SecretStr


class SettingsConfig(ConfigSection):
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_username: str | None = None
    redis_password: SecretStr | None = None
    throttling_rate: float = 1.0
    drop_pending_updates: bool = True


class Config(ConfigSection):
    bot: BotConfig
    settings: SettingsConfig = SettingsConfig()


def parse_config(config_file: str = "config.toml") -> Config:
    project_root = Path(__file__).resolve().parents[1]
    load_dotenv(project_root / ".env")

    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN environment variable is required")

    path = Path(config_file)
    if not path.is_absolute():
        path = Path.cwd() / path
    if path.suffix != ".toml" and not path.exists():
        path = path.with_suffix(".toml")
    if not path.is_file():
        raise FileNotFoundError(f"Config file not found: {path}")

    data = toml.loads(path.read_text(encoding="utf-8"))
    data.setdefault("bot", {})["token"] = token
    return Config.model_validate(data)
