import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('package_name', [
    'bdii',
    'glue-schema',
    'glite-info-provider-service']
)
def test_packages(host, package_name):
    package = host.package(package_name)

    assert package.is_installed


@pytest.mark.parametrize('bdii_file_path', [
    "/var/lib/bdii/gip/ldif",
    "/var/lib/bdii/gip/provider",
    "/var/lib/bdii/gip/plugin",
    "/var/run/bdii/db/"]
)
def test_required_paths(host, bdii_file_path):
    file = host.file(bdii_file_path)

    assert file.exists
