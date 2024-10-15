from pydantic import BaseModel
import datetime

class LogeventoCreate(BaseModel):
    descricao: str 
    tipo: str 
    usuario: str 

class LogEventoRespose(BaseModel):
    id: int
    descricao:str
    tipo: str
    data_criacao: datetime.datetime
    usuario: str


