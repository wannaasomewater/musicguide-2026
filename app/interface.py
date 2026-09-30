"""Вспомогательные функции интерфейса."""


def render_sources(documents: list[dict]) -> None:
    """Отрисовать список найденных документов (заглушка)."""
    for doc in documents:
        title = doc.get("title", "без названия")
        print(f"- {title}")


def render_answer(answer: str) -> None:
    """Отрисовать ответ LLM (заглушка)."""
    print(answer)
