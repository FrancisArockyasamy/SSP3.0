from pydantic_settings import BaseSettings, SettingsConfigDict
    
# env variable access code here
class Secret(BaseSettings):
    database: str
    dbuser: str
    password: str
    host: str
    port: str
    secret_key:str
    expire:int
    
    model_config= SettingsConfigDict(env_file=".env")
    
secret= Secret()

