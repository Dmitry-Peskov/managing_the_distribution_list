from pathlib import Path
from pydantic_settings import BaseSettings


class SettingsDB(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{Path(__file__).parent.parent}/database.sqlite3"
    echo: bool = True


settings_db = SettingsDB()
