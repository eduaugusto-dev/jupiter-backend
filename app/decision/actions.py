from enum import Enum


class Action(str, Enum):

    RESPOND_KNOWLEDGE = "respond_knowledge"

    QUERY_DATABASE = "query_database"

    BLOCK_ACCESS = "block_access"

    ASK_CLARIFICATION = "ask_clarification"