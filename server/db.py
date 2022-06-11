#!/usr/bin/python3

import psycopg
from psycopg.rows import dict_row
from dbtables import create_tables, insert_test_data

conn = psycopg.connect("dbname=pudding user=bproj password=bproj", row_factory=dict_row)

def fetch_pocs_for_stage(stage_id):
    cur = conn.cursor()
    sql = """
        SELECT
        poc.id,
        poc.name,
        stage_id,
        se_id,
        customer_id,
        stage.name as stage_name,
        customer.name as customer_name
        FROM poc
        LEFT JOIN stage ON stage.id = poc.stage_id
        LEFT JOIN customer on customer.id = poc.customer_id
        WHERE poc.stage_id = %s
    """
    cur.execute(sql, (stage_id,))
    return cur.fetchall()

def fetch_stages():
    cur = conn.cursor()
    sql = """
        SELECT *
        FROM stage
        ORDER BY id
    """
    try:
        cur.execute(sql)
    except psycopg.Error as e:
        print(e.diag.severity, e.diag.message_primary)
    try:
        return cur.fetchall()
    except psycopg.Error as e:
        print(e.diag.severity, e.diag.message_primary)
        return []



def fetch_pocs():
    cur = conn.cursor()
    sql = """
        SELECT
        poc.id,
        poc.name,
        stage_id,
        se_id,
        customer_id,
        stage.name as stage_name,
        customer.name as customer_name
        FROM poc
        LEFT JOIN stage ON stage.id = poc.stage_id
        LEFT JOIN customer on customer.id = poc.customer_id
    """
    cur.execute(sql)
    return cur.fetchall()


def fetch_one_poc(poc_id):
    cur = conn.cursor()
    cur.execute("SELECT * from poc WHERE id = %s", (poc_id,))
    return cur.fetchone()

def post_new_poc(poc):
    cur = conn.cursor()
    sql = """
        INSERT INTO poc (
        name,
        customer_id,
        stage_id,
        se_id
        ) VALUES (%s, %s, %s, %s)
        RETURNING *
    """
    cur.execute(sql, (poc.name, poc.customer_id, poc.stage_id, poc.se_id,))
    conn.commit()
    return cur.fetchone()

def update_poc(poc):
    cur = conn.cursor()
    sql = """
    UPDATE poc SET
    name = %s,
    customer_id = %s
    WHERE id = %s
    RETURNING *
    """
    cur.execute(sql,(poc.name, poc.customer_id, poc.id,))
    conn.commit()
    return cur.fetchone()

def delete_poc(poc_id):
    cur = conn.cursor()
    sql = """
    DELETE from poc
    WHERE id = %s
    """
    cur.execute(sql, (poc_id,))
    conn.commit()
    return {"result": "success"}

def fetch_uses_for_poc(poc_id):
    cur = conn.cursor()
    cur.execute("SELECT * from use WHERE poc_id = %s", (poc_id,))
    return cur.fetchall()

def post_new_use(poc_id, use):
    cur = conn.cursor()
    sql = """
        INSERT INTO use (
        name,
        description,
        seats,
        poc_id
        ) VALUES (%s, %s, %s, %s)
        RETURNING *
    """
    cur.execute(sql, (use.name, use.description, use.seats, use.poc_id,))
    conn.commit()
    return cur.fetchone()

def update_use(use):
    cur = conn.cursor()
    sql = """
    UPDATE use SET
    name = %s,
    description = %s,
    seats = %s
    WHERE id = %s
    RETURNING *
    """
    cur.execute(sql,(use.name, use.description, use.seats, use.id,))
    conn.commit()
    return cur.fetchone()

def fetch_customers():
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer")
    return cur.fetchall()

def fetch_one_customer(customer_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer WHERE id = %s", (customer_id,))
    return cur.fetchone()

def fetch_filtered_customers(search_term):
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer WHERE name LIKE %s", ('%'+search_term+'%',))
    return cur.fetchall()

def fetch_contacts(customer_id):
    cur = conn.cursor()
    sql = """
    with t as
    (
    SELECT
    contact.id as id,
    contact.first_name , contact.last_name , contact.title , 
    concat_ws(' ', contact.first_name, contact.last_name) as full_name,
    role.role
    from contact
    left join contact_role on contact.id = contact_role.contact_id
    left join role on contact_role.role_id = role.id
    where contact.customer_id = %s
    ORDER by contact.id
    )
    select id, full_name, last_name, first_name,
    title, string_agg(role, ',') as roles
    from t group by id, full_name, last_name, first_name, title
    """
    cur.execute(sql, (customer_id,))
    return cur.fetchall()

def post_new_contact(contact):
    cur = conn.cursor()
    sql = """
        INSERT INTO contact (
        first_name,
        last_name,
        title,
        customer_id
        ) VALUES (%s, %s, %s, %s)
        RETURNING *
    """
    cur.execute(sql, (contact.first_name, contact.last_name, contact.title, contact.customer_id,))
    conn.commit()
    new_contact = cur.fetchone()
    for role in contact.roles:
        sql = """
            INSERT INTO contact_role (
                contact_id,
                role_id
            ) VALUES (%s, %s)
        """
        cur.execute(sql, (new_contact["id"], role),)
    conn.commit()
    new_contact["roles"] = contact.roles
    return new_contact

def fetch_all_roles():
    cur = conn.cursor()
    sql = "SELECT * from role"
    cur.execute(sql)
    return cur.fetchall()

def fetch_all_verticals():
    cur = conn.cursor()
    cur.execute("SELECT * FROM vertical ORDER by id")
    return cur.fetchall()

def post_new_vertical(vertical):
    cur = conn.cursor()
    sql = """
        INSERT INTO vertical (
        name
        ) VALUES (%s)
        RETURNING *
    """
    cur.execute(sql, (vertical.name,))
    conn.commit()
    return cur.fetchone()

def update_vertical(vertical):
    cur = conn.cursor()
    sql = """
    UPDATE vertical SET
    name = %s
    WHERE id = %s
    RETURNING *
    """
    cur.execute(sql,(vertical.name, vertical.id,))
    conn.commit()
    return cur.fetchone()


if __name__ == "__main__":
    create_tables(conn, cur)
    insert_test_data(conn, cur)
    conn.close()