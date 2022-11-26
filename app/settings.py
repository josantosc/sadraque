from decouple import config

ATLAS_URI = config("ATLAS_URI", default="localhost")
DB_NAME = config("DB_NAME", default="db-sadraque")