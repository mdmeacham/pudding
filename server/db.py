#!/usr/bin/python3

import psycopg
from psycopg.rows import dict_row
from dbtables import create_tables, insert_test_data

conn = psycopg.connect("dbname=pudding user=bproj password=bproj", row_factory=dict_row)
cur = conn.cursor()

def fetch_pocs_for_stage(stage_id):
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

def fetch_one_poc(poc_id):
    cur.execute("SELECT * from poc WHERE id = %s", (poc_id,))
    return cur.fetchone()

def post_new_poc(poc):
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
    sql = """
    DELETE from poc
    WHERE id = %s
    """
    cur.execute(sql, (poc_id,))
    conn.commit()
    return {"result": "success"}

def fetch_uses_for_poc(poc_id):
    cur.execute("SELECT * from use WHERE poc_id = %s", (poc_id,))
    return cur.fetchall()

def post_new_use(poc_id, use):
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
    cur.execute("SELECT * FROM customer")
    return cur.fetchall()

def fetch_one_customer(customer_id):
    cur.execute("SELECT * FROM customer WHERE id = %s", (customer_id,))
    return cur.fetchone()

def fetch_filtered_customers(search_term):
    cur.execute("SELECT * FROM customer WHERE name LIKE %s", ('%'+search_term+'%',))
    return cur.fetchall()

def fetch_contacts(customer_id):
    sql = """
    SELECT
    contact.first_name , contact.last_name , contact.title , 
    concat_ws(' ', contact.first_name, contact.last_name) as full_name,
    role.role
    from contact
    left join contact_role on contact.id = contact_role.contact_id
    left join role on contact_role.role_id = role.id
    where contact.customer_id = %s
    ORDER by contact.id
    """
    cur.execute(sql, (customer_id,))
    return cur.fetchall()

if __name__ == "__main__":
    create_tables(conn, cur)
    insert_test_data(conn, cur)
    conn.close()