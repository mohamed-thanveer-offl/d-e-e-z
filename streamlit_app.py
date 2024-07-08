# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import pandas as pd

from PIL import Image

# Function to load icons
def load_icon(icon_name):
    return Image.open(icon_name)

# Dropdown options with icons
sources = {
    "Blob": load_icon("icons/blob.png"),
    "MS SQL Server": load_icon("icons/mssql.png"),
    "Postgres SQL Server": load_icon("icons/postgres.png"),
    "Oracle SQL Server": load_icon("icons/oracle.png")
}

def main_page():

    st.title("D-E-E-Z")

    st.markdown("#### Use Data Engineering E Z (a.k.a Easy) to ease your engineering process 🖥️")

def extract():

    # Select Source
    source = st.selectbox("Select Source", options=list(sources.keys()), format_func=lambda x: x, index=0)

    # Display icon for selected source
    st.image(sources[source], width=50)

    # Variables to store user inputs
    blob_config = {}
    mssql_config = {}
    postgres_config = {}
    oracle_config = {}

    # Form based on selected source
    if source == "Blob":
        st.header("Blob Configuration")
        blob_config['account_name'] = st.text_input("Account Name")
        blob_config['account_key'] = st.text_input("Account Key", type="password")
        blob_config['container_name'] = st.text_input("Container Name")
        # Add other Blob specific fields

    elif source == "MS SQL Server":
        st.header("MS SQL Server Configuration")
        mssql_config['server'] = st.text_input("Server")
        mssql_config['database'] = st.text_input("Database")
        mssql_config['username'] = st.text_input("Username")
        mssql_config['password'] = st.text_input("Password", type="password")
        # Add other MS SQL Server specific fields

    elif source == "Postgres SQL Server":
        st.header("Postgres SQL Server Configuration")
        postgres_config['host'] = st.text_input("Host")
        postgres_config['database'] = st.text_input("Database")
        postgres_config['user'] = st.text_input("User")
        postgres_config['password'] = st.text_input("Password", type="password")
        postgres_config['port'] = st.number_input("Port", value=5432)
        # Add other Postgres SQL Server specific fields

    elif source == "Oracle SQL Server":
        st.header("Oracle SQL Server Configuration")
        oracle_config['host'] = st.text_input("Host")
        oracle_config['port'] = st.number_input("Port", value=1521)
        oracle_config['service_name'] = st.text_input("Service Name")
        oracle_config['user'] = st.text_input("User")
        oracle_config['password'] = st.text_input("Password", type="password")
        # Add other Oracle SQL Server specific fields

    # Submit button
    if st.button("Submit"):
        st.success(f"{source} configuration submitted successfully!")

        # Generate and display Python code to connect to the respective source
        if source == "Blob":
            blob_code = f"""
    import os
    from azure.storage.blob import BlobServiceClient

    account_name = "{blob_config['account_name']}"
    account_key = "{blob_config['account_key']}"
    container_name = "{blob_config['container_name']}"

    connection_string = f"DefaultEndpointsProtocol=https;AccountName={{account_name}};AccountKey={{account_key}};EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    """
            st.code(blob_code, language='python')

        elif source == "MS SQL Server":
            mssql_code = f"""
    import pyodbc

    server = "{mssql_config['server']}"
    database = "{mssql_config['database']}"
    username = "{mssql_config['username']}"
    password = "{mssql_config['password']}"

    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={{server}};DATABASE={{database}};UID={{username}};PWD={{password}}"
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    """
            st.code(mssql_code, language='python')

        elif source == "Postgres SQL Server":
            postgres_code = f"""
    import psycopg2

    host = "{postgres_config['host']}"
    database = "{postgres_config['database']}"
    user = "{postgres_config['user']}"
    password = "{postgres_config['password']}"
    port = {postgres_config['port']}

    conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
    cursor = conn.cursor()
    """
            st.code(postgres_code, language='python')

        elif source == "Oracle SQL Server":
            oracle_code = f"""
    import cx_Oracle

    host = "{oracle_config['host']}"
    port = {oracle_config['port']}
    service_name = "{oracle_config['service_name']}"
    user = "{oracle_config['user']}"
    password = "{oracle_config['password']}"

    dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
    conn = cx_Oracle.connect(user=user, password=password, dsn=dsn)
    cursor = conn.cursor()
    """
            st.code(oracle_code, language='python')
    # uploaded_file = st.file_uploader('Choose a file')
    # if uploaded_file is not None:
    #     #read csv
    #     df1 = pd.read_csv(uploaded_file)


def load():
    st.markdown("# Load ⬆️")

def transform():
    st.markdown("# Transform 🔄")

page_names_to_funcs = {
    "Home": main_page,
    "Extract": extract,
    "Load": load,
    "Transform": transform,
}

selected_page = st.sidebar.selectbox("Select E-L-T", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()