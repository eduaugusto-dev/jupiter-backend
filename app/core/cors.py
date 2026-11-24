
from fastapi.middleware.cors import CORSMiddleware


def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://localhost:8080",
            "http://localhost:5173",
            "http://127.0.0.1:8787",
            "http://localhost:8787",
            "https://seguraoz.lovable.app",
        ],
        allow_origin_regex=r"https://.*\.vercel\.app",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

