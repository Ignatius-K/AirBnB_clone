"""__init__ for models package"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
