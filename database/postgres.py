def connection_string(host,db,user,password,port=5432):
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"
