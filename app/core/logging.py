import sys
from pathlib import Path

from loguru import logger

from app.core.config import settings


LOG_PATH = Path("logs")

LOG_PATH.mkdir(
    exist_ok=True
)


def setup_logging():
    """
    Configuração central do sistema de logs.
    """

    logger.remove()


    # Console
    logger.add(
        sys.stdout,
        level=settings.LOG_LEVEL,
        colorize=True,
        format=
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level}</level> | "
        "{message}",
    )


    # Log geral da aplicação
    logger.add(
        LOG_PATH / "app.log",
        level="INFO",
        rotation="10 MB",
        retention="30 days",
        encoding="utf-8",
    )


    # Log de erros
    logger.add(
        LOG_PATH / "errors.log",
        level="ERROR",
        rotation="10 MB",
        retention="30 days",
        encoding="utf-8",
    )


    logger.info(
        f"{settings.APP_NAME} - Logging iniciado"
    )


    return logger