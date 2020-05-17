from App.exts import db

class BaseModel(db.Model):
    
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' %(table_name, column_name, column_type))

def drop_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    engine.execute('ALTER TABLE %s DROP COLUMN %s' %(table_name, column_name))
