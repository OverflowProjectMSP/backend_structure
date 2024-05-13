import os
import uuid
import psycopg2
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
import random
from datetime import datetime
from dotenv import load_dotenv
import base64
import logging

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

try: 
    pg = psycopg2.connect(f"""
        host=localhost
        dbname=postgres
        user=postgres
        password={os.getenv('PASSWORD_PG')}
        port={os.getenv('PORT_PG')}
    """)

    cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute(f"SELECT COUNT() from users")
    print(cursor.fetchone()[0])



except (Exception, Error) as error:
    logging.error(f'DB: ', error)
    return_data = f"Ошибка обращения к базе данных: {error}" 

finally:
    if pg:
        cursor.close
        pg.close
        logging.info("Соединение с PostgreSQL закрыто")
