def create_tables(conn, cur):
    cur.execute("DROP TABLE IF EXISTS contact_role CASCADE")
    cur.execute("DROP TABLE IF EXISTS role CASCADE")
    cur.execute("DROP TABLE IF EXISTS contact CASCADE")
    cur.execute("DROP TABLE IF EXISTS role CASCADE")
    cur.execute("DROP TABLE IF EXISTS customer CASCADE")
    cur.execute("DROP TABLE IF EXISTS se CASCADE")
    cur.execute("DROP TABLE IF EXISTS stage CASCADE")
    cur.execute("DROP TABLE IF EXISTS poc CASCADE")

    conn.commit()    


    cur.execute(
        """
        CREATE TABLE stage (
        id serial PRIMARY KEY,
        name text)
        """
    )

    cur.execute(
        """
        CREATE TABLE se (
        id serial PRIMARY KEY,
        first_name text,
        last_name text,
        team text)
        """
    )

    cur.execute(
        """
        CREATE TABLE customer (
        id serial PRIMARY KEY,
        name text)
        """
    )

    cur.execute(
        """
        CREATE TABLE poc (
        id serial PRIMARY KEY,
        name text,
        customer_id int,
        stage_id int,
        se_id int,
        CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customer(id),
        CONSTRAINT fk_stage FOREIGN KEY(stage_id) REFERENCES stage(id),
        CONSTRAINT fk_se FOREIGN KEY(se_id) REFERENCES se(id)
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE use (
            id serial PRIMARY KEY,
            name text,
            description text,
            seats int,
            poc_id int,
            CONSTRAINT fk_poc FOREIGN KEY(poc_id) REFERENCES poc(id)
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE contact (
        id serial PRIMARY KEY,
        first_name text,
        last_name text,
        title text,
        customer_id int,
        CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customer(id)
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE role (
        id serial PRIMARY KEY,
        role text
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE contact_role (
        contact_id int,
        role_id int,
        PRIMARY KEY(role_id, contact_id),
        CONSTRAINT fk_contact FOREIGN KEY(contact_id) REFERENCES contact(id),
        CONSTRAINT fk_role FOREIGN KEY(role_id) REFERENCES role(id)
        )
        """
    )

    conn.commit()


def insert_test_data(conn, cur):
    sql = """
        INSERT INTO stage (
        name) VALUES (%s);
    """
    stages = [
        {"name": "In Execution"},
        {"name": "In Preparation"},
        {"name": "On Hold"},
        {"name": "Completed"},
        {"name": "Canceled"},
    ]
    for stage in stages:
        cur.execute(sql, (stage['name'],))

    sql = """
        INSERT INTO se (
        first_name,
        last_name,
        team) VALUES (%s, %s, %s);
    """
    ses = [
        {"first_name": "Mike", "last_name": "Meacham", "team": "US Northwest"},
        {"first_name": "Carl", "last_name": "Segan", "team": "Outer Rim"},
    ]
    for se in ses:
        cur.execute(sql, (se['first_name'],se['last_name'], se['team']))

    sql = """
        INSERT INTO role (role) VALUES (%s);
    """
    roles = [
        {"role": "Technical evaluator"},
        {"role": "Technical decision maker"},
        {"role": "Business decision maker"},
    ]
    for role in roles:
        cur.execute(sql, (role['role'],))

    sql = """
        INSERT INTO customer (name) VALUES (%s);
    """
    customers = [
        {"name": "UW Medicine"},
        {"name": "Costco"},
        {"name": "Seattle Children's"},
    ]
    for customer in customers:
        cur.execute(sql, (customer['name'],))

    sql = """
        INSERT INTO poc (
        name,
        customer_id,
        stage_id,
        se_id
        ) VALUES (%s, %s, %s, %s)
    """

    pocs = [
        {
            "name": "WFH coders",
            "customer_id": 1,
            "stage_id": 1,
            "se_id": 1
        }
    ]

    for poc in pocs:
        cur.execute(sql, (poc['name'], poc['customer_id'], poc['stage_id'], poc['se_id']))

    sql = """
        INSERT INTO use (
        name,
        description,
        seats,
        poc_id
        ) VALUES (%s, %s, %s, %s)
    """

    uses = [
        {
            "name": "Home coders",
            "description": "These users are at home and are doing coding for insurance billing",
            "seats": 1000,
            "poc_id": 1
        }
    ]

    for use in uses:
        cur.execute(sql, (use['name'], use['description'], use['seats'], use['poc_id']))

    sql = """
        INSERT INTO contact (
        first_name,
        last_name,
        title,
        customer_id
        ) VALUES (%s, %s, %s, %s);
    """
    contacts = [
        {
            "first_name": "Gordon",
            "last_name": "Lightfoot",
            "title": "Systems Engineer",
            "customer_id": "1"
        },
        {
            "first_name": "Michael",
            "last_name": "Jordan",
            "title": "EUC Engineer",
            "customer_id": "1"
        },
        {
            "first_name": "Captain",
            "last_name": "America",
            "title": "Director of IT",
            "customer_id": "1"
        },
    ]
    for contact in contacts:
        cur.execute(
            sql, 
            (
                contact['first_name'],
                contact['last_name'],
                contact['title'],
                contact['customer_id'],
            )
        )

    sql = """
    INSERT INTO contact_role (
    contact_id,
    role_id
    ) Values (%s, %s);
    """

    cur.execute(sql, (1,1)) # Gordon Lightfoot is a technical evaluator
    cur.execute(sql, (1,2)) # Gordon Lightfoot is also a technical decision maker
    cur.execute(sql, (2,1)) # Michael Jordan is a technical evaluator
    cur.execute(sql, (3,3)) # Captain America is a Business decision maker

    conn.commit()


