#!/usr/bin/python3
"""
Initializing the engine package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()