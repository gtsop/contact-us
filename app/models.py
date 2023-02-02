from sqlalchemy import Boolean, Column, Integer, String
import ipaddress

from .database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    ipv4 = Column(String(15), nullable=False, index=True)
    email = Column(String)
    body = Column(String)

    # @validates('ip')
    # def validate_ip(self, key, address):
    #     if not isinstance(address, ipaddress.IPv4Address):
    #         raise ValueError(f"Invalid IPv4 address: {address}")
    #     return str(address)
