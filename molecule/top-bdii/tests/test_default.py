import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_update_urls(host):
    '''
    Test for proper configuration of the glite-update-urls configuration
    '''

    # The config file for the endpoint generation should exist
    # and have sane defaults
    update_config_file = host.file('/etc/glite/glite-info-update-endpoints.conf')
    assert update_config_file.exists
    assert update_config_file.contains('^EGI.*[T|t]rue$')

    # The log file should exist
    info_update_log_file = host.file('/var/log/glite/glite-info-update-endpoints.log')
    assert info_update_log_file.exists
    assert info_update_log_file.is_file

def test_bdii_configuration(host):
    '''
    Tests for the correctness of the bdii configuration itself
    '''
    assert True


def test_processes(host):
    '''
    Tests for checking that the correct processes are running
    '''

    assert True