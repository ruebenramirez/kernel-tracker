from sqlalchemy import Column, Integer, String
import sqlite3

conn = sqlite3.connect('kernel-tracker.db')

class KernelVersion(Base):
    __tablename__ = 'kernel_versions'

    id = Column(Integer, primary_key=True)
    version = Column(String)

    def __init__(self, version):
        self.version = version

