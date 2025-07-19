from pydantic import BaseModel


class PersonSchema(BaseModel):
    codigo_pessoa: int
    nome_pessoa: str

    class Config:
        orm_mode = True
