# Benchmark — MusicGuide

Набор вопросов для оценки RAG-пайплайна.

## Формат
JSONL, одна строка = один вопрос:

    {"id": 1, "question": "...", "gold_doc_ids": ["..."], "reference_answer": "..."}

## Метрики
- Precision@5
- Recall@5
- MRR
- Faithfulness

## Запуск (план)

    python -m benchmark.run
