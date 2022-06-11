from fastapi.middleware.cors import CORSMiddleware

def configure_cors(app):
    origins = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:8081",
        "http://localhost:3000",
        "http://localhost:9000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
