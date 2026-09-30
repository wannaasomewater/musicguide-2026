"""Smoke-тесты: проверяют, что приложение импортируется и запускается."""

import app


def test_version_exists():
    assert app.__version__ == "0.1.0"


def test_import_interface():
    from app import interface
    assert hasattr(interface, "render_sources")
    assert hasattr(interface, "render_answer")
