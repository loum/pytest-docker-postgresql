"""Shakeout the PostgreSQL docker instance.

"""
import json
import pytest


# @pytest.mark.skipif(raises=Exception)
def test_docker_pg_conn(pg_conn):
    """Test a pristine PostgreSQL instance.
    """
    # Get PostgreSQL version
    cursor = pg_conn.cursor()
    cursor.execute('SELECT version()')
    received = cursor.fetchall()

    msg = 'Pristine PostgreSQL version check did not return a response'
    assert received, msg
