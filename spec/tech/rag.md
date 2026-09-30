# RAG-пайплайн

## Корпус
- Источник: Kaggle — 500K+ Spotify Songs with Lyrics, Emotions & More.
- Формат: JSONL, поля: id, title, artist, album, genre, text, source_url.
- Объём на КТ-1: черновик; на финал — 200–1000 документов.

## Индексация
- Токенизация: нижний регистр, удаление стоп-слов, лемматизация (pymorphy3).
- BM25: k1=1.5, b=0.75.

## Поиск
- top-k = 5 фрагментов.

## Генерация
- Промпт: «Ответь на вопрос, используя только фрагменты ниже.
  Если ответа нет — скажи об этом. Укажи источники.»
- LLM: локальная (Ollama) или внешний API.

## Benchmark
- 30–50 вопросов.
- Метрики: Precision@5, Recall@5, MRR, faithfulness.
- Файл: benchmark/questions.jsonl
