from pathlib import Path
from pydantic_settings import BaseSettings


class SettingsDB(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{Path(__file__).parent.parent}/database.sqlite3"
    echo: bool = True


class SettingsAPI(BaseSettings):
    api_v1_prefix: str = "/api/v1"


settings_db = SettingsDB()
settings_api = SettingsAPI()
