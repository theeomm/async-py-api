from functools import lru_cache

from app.conf import Settings


@lru_cache
def get_settings():
  return Settings()
