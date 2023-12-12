from fastapi import FastAPI
from api_v1 import router as router_v1
from core.config import settings_api


app = FastAPI(title="Система управления распределением задач",
              summary="Интерфейс, позваляющий управлять распределением поступающих задач среди персонала подразделения",
              version="0.1.0",
              )

app.include_router(router=router_v1, prefix=settings_api.api_v1_prefix)
