from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from app.api.v1.router import router as v1_router

def load_all_models() -> None:
    """Load all models from `app.api.v1`.
    Models must be in app/api/v1/*/models.py to be imported.
    """

    # Converts absolute path of a file ending in `models.py` to an import
    def path_to_import(p):
        return p[p.find("app") :].split(".py")[0].replace("/", ".")

    # Sort to make sure we don't have random circular imports
    model_paths = Path(__file__).parent.glob("api/v1/**/models.py")
    model_paths = list(model_paths)
    model_paths.sort()

    for path in model_paths:
        module_name = path_to_import(str(path))
        __import__(module_name)


def get_app() -> FastAPI:
    app = FastAPI(
        title="Omnilore Data Gathering API",
        description="API for gathering data for Omnilore's Membership Database",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    load_all_models()

    app.include_router(v1_router)

    return app