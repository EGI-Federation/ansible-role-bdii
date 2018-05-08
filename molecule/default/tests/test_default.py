import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# The process should be run by the openldap user
def test_slapd_user(host):
    user = host.user('openldap')

    assert user.exists
    assert user.shell == '/usr/sbin/nologin'


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


# def test_slapd_process(host):
#     slapd_process = host.process.filter(comm="slapd")
#     assert slapd_process.running
#     slapd_port = "tcp://0.0.0.0:2170"
#     assert host.socket(slapd_port).is_listening


def test_config_files(host):
    bdii_update_script = host.file('/usr/sbin/bdii-update')
    bdii_conf = host.file('/etc/bdii/bdii.conf')

    assert bdii_update_script.exists
    assert bdii_update_script.is_file
    assert bdii_update_script.mode == 777

    assert bdii_conf.exists
    assert bdii_conf.is_file
    # contains ?


def test_log_files(host):
    bdii_log_dir = host.file('/var/log/bdii')
    bdii_log_file = host.file('/var/log/bdii/bdii-update.log')

    assert bdii_log_dir.exists
    assert bdii_log_dir.is_dir
    assert bdii_log_dir.owner == 'openldap'

    assert bdii_log_file.exists
    assert bdii_log_file.is_file
    assert bdii_log_file.owner


def test_data_files(host):
    data_dir = host.file('/var/lib/bdii')

    assert data_dir.exists
    assert data_dir.is_directory
    assert data_dir.user == 'openldap'


def test_cron_jobs(host):
    # top-bdii update cron
    assert True

# def security(host):
# database is world-readable but modifiable only by root
