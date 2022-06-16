from database.config import SessionLocal


# Dependency
def get_db():
    """管理数据库连接，使用后自动关闭连接"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
