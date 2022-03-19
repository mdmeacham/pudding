def create_tables(conn, cur):
    cur.execute("DROP TABLE IF EXISTS contact_role CASCADE")
    cur.execute("DROP TABLE IF EXISTS role CASCADE")
    cur.execute("DROP TABLE IF EXISTS contact CASCADE")
    cur.execute("DROP TABLE IF EXISTS contact_role CASCADE")
    cur.execute("DROP TABLE IF EXISTS customer CASCADE")
    cur.execute("DROP TABLE IF EXISTS se CASCADE")
    cur.execute("DROP TABLE IF EXISTS team CASCADE")
    cur.execute("DROP TABLE IF EXISTS stage CASCADE")
    cur.execute("DROP TABLE IF EXISTS poc CASCADE")
    cur.execute("DROP TABLE IF EXISTS use CASCADE")
    cur.execute("DROP TABLE IF EXISTS poc_use CASCADE")
    cur.execute("DROP TABLE IF EXISTS vertical CASCADE")
    cur.execute("DROP TABLE IF EXISTS use_vertical CASCADE")
    cur.execute("DROP TABLE IF EXISTS third_party CASCADE")
    cur.execute("DROP TABLE IF EXISTS use_third_party CASCADE")
    cur.execute("DROP TABLE IF EXISTS poc_third_party CASCADE")

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
        CREATE TABLE team (
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
        team_id int,
        CONSTRAINT fk_team FOREIGN KEY(team_id) REFERENCES team(id))
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
        CREATE TABLE vertical (
            id serial PRIMARY KEY,
            name text
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE third_party (
        id serial PRIMARY KEY,
        name text
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE use (
        id serial PRIMARY KEY,
        name text,
        description text
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE use_vertical (
        use_id int,
        vertical_id int,
        PRIMARY KEY(use_id, vertical_id),
        CONSTRAINT fk_use FOREIGN KEY(use_id) REFERENCES use(id),
        CONSTRAINT fk_vertical FOREIGN KEY(vertical_id) REFERENCES vertical(id)
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE poc_use (
        poc_id int,
        use_id int,
        seats int,
        notes text,
        PRIMARY KEY(poc_id, use_id),
        CONSTRAINT fk_poc FOREIGN KEY(poc_id) REFERENCES poc(id),
        CONSTRAINT fk_use FOREIGN KEY(use_id) REFERENCES use(id)
        )
        """
    )

    cur.execute( # Possible third party products for a use
        """
        CREATE TABLE use_third_party (
        use_id int,
        third_party_id int,
        PRIMARY KEY(use_id, third_party_id),
        CONSTRAINT fk_use FOREIGN KEY(use_id) REFERENCES use(id),
        CONSTRAINT fk_third_party FOREIGN KEY(third_party_id) REFERENCES third_party(id)
        )
        """
    )

    cur.execute( # Actual third party products for use case in this POC
        """
        CREATE TABLE poc_third_party (
        poc_id int,
        third_party_id int,
        PRIMARY KEY(poc_id, third_party_id),
        CONSTRAINT fk_poc FOREIGN KEY(poc_id) REFERENCES poc(id),
        CONSTRAINT fk_third_party FOREIGN KEY(third_party_id) REFERENCES third_party(id)
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
        INSERT INTO team (
            name
        ) values (%s)
    """

    teams = ["NA Northwest", "NA Southwest"]

    for team in teams:
        cur.execute(sql, (team,))

    sql = """
        INSERT INTO se (
        first_name,
        last_name,
        team_id) VALUES (%s, %s, %s);
    """
    ses = [
        {"first_name": "Mike", "last_name": "Meacham", "team_id": 1},
        {"first_name": "Carl", "last_name": "Segan", "team_id": 2},
    ]
    for se in ses:
        cur.execute(sql, (se['first_name'],se['last_name'], se['team_id'],))

    sql = """
        INSERT INTO role (role) VALUES (%s);
    """
    roles = [
        {"role": "Technical evaluator"},
        {"role": "Technical decision maker"},
        {"role": "Business decision maker"},
        {"role": "Executive decision maker"},
        {"role": "Project manager"},
    ]
    for role in roles:
        cur.execute(sql, (role['role'],))

    sql = """
        INSERT INTO customer (name) VALUES (%s);
    """
    customers = [
        {"name": "Dark Ages Medical"},
        {"name": "1 cent store"},
        {"name": "Best of Rest Health"},
    ]
    for customer in customers:
        cur.execute(sql, (customer['name'],))


    sql = """
        INSERT INTO vertical (
        name    
        ) VALUES (%s)
    """

    verticals = [
        "Healthcare",
        "Retail",
        "Finance",
        "Upper education",
        "K-12",
        "Government"
    ]

    for vertical in verticals:
        cur.execute(sql, (vertical,))

    sql = """
        INSERT INTO use (
        name,
        description
        ) VALUES (%s, %s)
    """

    uses = [
        {
            "name": "Home coders",
            "description": "These users are at home and are doing coding for insurance billing"
        },
        {
            "name": "Workstations on wheels",
            "description": "These are carts that freely move around the hospital.  Wi-Fi is used"
        },
        {
            "name": "Nurse stations",
            "description": "Pods of end points that are not in the clinic rooms and that are mostly used by nurses"
        }
    ]

    for use in uses:
        cur.execute(sql, (use['name'], use['description'],))

    sql = """
        INSERT INTO use_vertical (
        use_id,
        vertical_id
        ) VALUES (%s, %s)
    """

    use_verticals = [
        {"use_id": 1, "vertical_id": 1},
        {"use_id": 2, "vertical_id": 1},
        {"use_id": 3, "vertical_id": 1},
    ]

    sql = """
        INSERT INTO third_party (
            name
        ) VALUES (%s)
    """

    products = [
        {"name": "Citrix Xen Desktop"},
        {"name": "Citrix Xen App"},
        {"name": "VMware Horizon"},
        {"name": "Imprivata"},
        {"name": "Nuance PowerMIC III"},
        {"name": "Microsoft RDS"}
    ]

    for product in products:
        cur.execute(sql, (product['name'],))

    # Use Third Party # 1 is home coders 2 is WOW 3 is nurse stations

    sql = """
        INSERT INTO use_third_party (
        use_id,
        third_party_id
        ) VALUES (%s, %s)
    """
    use_third_parties = [
        {"use_id": 1, "third_party_id": 1},
        {"use_id": 1, "third_party_id": 2},
        {"use_id": 2, "third_party_id": 1},
        {"use_id": 2, "third_party_id": 2},
        {"use_id": 3, "third_party_id": 1},
        {"use_id": 3, "third_party_id": 2},
        {"use_id": 3, "third_party_id": 4}
    ]

    for use_third_party in use_third_parties:
        cur.execute(sql, (use_third_party["use_id"], use_third_party["third_party_id"],))

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
        INSERT INTO poc_third_party (
        poc_id,
        third_party_id
        ) VALUES (%s, %s)
    """

    poc_third_parties = [
        {"poc_id": 1, "third_party_id": 1}
    ]

    for poc_third_party in poc_third_parties:
        cur.execute(sql, (poc_third_party["poc_id"], poc_third_party["third_party_id"],))


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
        {
            "first_name": "Bruce",
            "last_name": "Wayne",
            "title": "Project manager",
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
    cur.execute(sql, (4,5)) # Bruce Wayne is a project manager

    conn.commit()


