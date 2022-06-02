from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
from time import sleep
from app.routes import quote
from app import env

while True:
    try:
        conn = psycopg2.connect( host=env.database_host_name, port= env.database_port , database=env.database_name, user=env.database_user_name, password=env.database_password, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("databse connection successfull")
        break
    except Exception as error:
        print(error)
        sleep(1)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(quote.router)



