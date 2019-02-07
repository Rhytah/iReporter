sqlcommands = (

    """
                CREATE TABLE IF NOT EXISTS users(
                    userid SERIAL PRIMARY KEY,
                    firstname VARCHAR (30),
                    lastname VARCHAR (30),
                    username VARCHAR (30),
                    password VARCHAR (20),
                    email VARCHAR (30),
                    isadmin BOOLEAN DEFAULT FALSE NOT NULL,
                    registered TIMESTAMP DEFAULT NOW()
                    )
                """,
    """
                CREATE TABLE IF NOT EXISTS redflags(
                    redflag_id SERIAL PRIMARY KEY,
                    created_by INT REFERENCES users(userid),
                    created_on TIMESTAMP,
                    image VARCHAR(255),
                    video VARCHAR (255),
                    location VARCHAR(255), 
                    status VARCHAR (15),
                    comment VARCHAR (225)
                    )
                """,
    """
                CREATE TABLE IF NOT EXISTS interventions(
                    intervention_id SERIAL PRIMARY KEY,
                    created_by INT REFERENCES users(userid),
                    created_on TIMESTAMP,
                    location VARCHAR(255),
                    image VARCHAR(225),
                    video VARCHAR (255),
                    status VARCHAR(15),
                    comment VARCHAR (255)
                    )
                """,

    """
                INSERT INTO users(firstname,lastname,username, password,email, isadmin)      
                VALUES('Rhytah','Namono','admin','sup3rpsW','girl@world.com' ,True)                
                """
)
