class Config:

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1055@host.docker.internal:3306/db_edificios'



    SQLALCHEMY_TRACK_MODIFICATIONS = False


    SECRET_KEY = 'super_secret_key_change_me'