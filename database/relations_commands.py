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
                    incident_type VARCHAR (30) NOT NULL,
                    location FLOAT8, 
                    status VARCHAR (15),
                    comment VARCHAR (225)
                    )
                """,
                """
                CREATE TABLE IF NOT EXISTS interventions(
                    intervention_id SERIAL PRIMARY KEY,
                    created_by INT REFERENCES users(userid),
                    created_on TIMESTAMP,
                    incident_type VARCHAR (30) NOT NULL,
                    location FLOAT8, 
                    status VARCHAR(15),
                    comment VARCHAR (225)
                    )
                """,
                
                """
                INSERT INTO users(username, password, isadmin)      
                VALUES('admin','sup3rpsW' ,True)
                """,
                """
                INSERT INTO users(username, password, isadmin)
                VALUES('nonadmin','in1tial', False)
                
                """
)