from fastapi import FastAPI

from app.api.router import api_router
from app.core.cors import configure_cors


app = FastAPI(
    title="Júpiter - Agente de RH",
    description="Agente inteligente de atendimento interno de RH da SeguraOz",
    version="1.0.0",
)

# Configuração de comunicação com o frontend (v0 / Vercel).
configure_cors(app)

# As tabelas e os dados são gerenciados exclusivamente pelo Supabase.
# Não executar create_all, seeds ou inicialização de banco local no startup.
app.include_router(api_router)
