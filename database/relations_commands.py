sqlcommands = (    
                              
                """
                CREATE TABLE IF NOT EXISTS users(
                    userid SERIAL PRIMARY KEY,
                    firstname VARCHAR (30),
                    lastname VARCHAR (30),
                    username VARCHAR (30),
                    password VARCHAR (10),
                    email VARCHAR (30),
                    phone_number BIGINT,
                    isadmin BOOLEAN DEFAULT FALSE NOT NULL,
                    registered TIMESTAMP DEFAULT NOW()
                    )
                """,
                """
                CREATE TABLE IF NOT EXISTS redflags(
                    redflag_id SERIAL PRIMARY KEY,
                    created_by INT REFERENCES users(userid),
                    created_on TIMESTAMP,
                    image VARCHAR(100),
                    video VARCHAR (100),
                    lat FLOAT8,
                    long FLOAT8, 
                    status VARCHAR (30),
                    comment VARCHAR (225)
                    )
                """,
                """
                CREATE TABLE IF NOT EXISTS interventions(
                    intervention_id SERIAL PRIMARY KEY,
                    created_by INT REFERENCES users(userid),
                    created_on TIMESTAMP,
                    lat FLOAT8,
                    long FLOAT8,
                    image VARCHAR(100),
                    video VARCHAR (100),
                    status VARCHAR(30),
                    comment VARCHAR (225)
                    )
                """,
                
                """
                INSERT INTO users(firstname,lastname,username, password,email,phone_number, isadmin)      
                VALUES('Rhytah','Namono','admin','sup3rpsW','girl@world.com',8562438 ,True)                
                """
)