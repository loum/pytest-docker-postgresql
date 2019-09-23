"""Docker PostgreSQL fixtures.

"""
import os
import pytest
import struct
import pg8000
import backoff
from lovely.pytest.docker.compose import Services


@pytest.fixture(scope='session')
def postgresql_docker_compose_files(pytestconfig):
    """Get the docker-compose.yml absolute path.
    """
    dirname = os.path.dirname(__file__)
    return [
        os.path.join(dirname,
                     'pytest_docker_postgresql',
                     'docker',
                     'docker-compose.yml'),
    ]


@pytest.fixture(scope='session')
def postgresql_docker_services(request,
                               pytestconfig,
                               postgresql_docker_compose_files,
                               docker_ip):
    """Provide the docker services as a pytest fixture.

    The services will be stopped after all tests are run.
    """
    keep_alive = request.config.getoption("--keepalive", False)
    project_name = "pytest{}".format(str(pytestconfig.rootdir))
    services = Services(postgresql_docker_compose_files,
                        docker_ip,
                        project_name)
    yield services
    if not keep_alive:
        services.shutdown()


@pytest.fixture(scope='session')
def pg_conn(postgresql_docker_services):
    postgresql_docker_services.start('postgresql')
    postgresql_docker_services.wait_for_service('postgresql',
                                                5432,
                                                check_server=custom_service_checker)

    import time
    time.sleep(10)

    conn = pg8000.connect(user='postgres', password='postgres')

    return conn


@backoff.on_exception(backoff.expo, struct.error)
def custom_service_checker(ip_address, port):
    return pg8000.connect(user='postgres', password='postgres')
