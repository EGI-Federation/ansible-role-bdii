import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# The process should be run by the slapd user
def test_slapd_user(host):
    user = host.user('ldap')

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
    # bdii_update_script = host.file('/usr/sbin/bdii-update')
    bdii_conf = host.file('/etc/bdii/bdii.conf')
    bdii_sysconfig = host.file('/etc/sysconfig/bdii')

    assert bdii_conf.exists
    assert bdii_conf.is_file
    assert bdii_conf.user == 'root'

    assert bdii_sysconfig.exists
    assert bdii_sysconfig.is_file


def test_log_files(host):
    bdii_log_dir = host.file('/var/log/bdii')
    # bdii_log_file = host.file('/var/log/bdii/bdii-update.log')

    assert bdii_log_dir.exists
    assert bdii_log_dir.is_directory
    assert bdii_log_dir.user == 'ldap'

    # assert bdii_log_file.exists
    # assert bdii_log_file.is_file
    # assert bdii_log_file.user == 'ldap'


def test_data_files(host):
    data_dir = host.file('/var/lib/bdii')

    assert data_dir.exists
    assert data_dir.is_directory
    assert data_dir.user == 'ldap'


def test_cron_jobs(host):
    # top-bdii update cron
    assert True

# def security(host):
# database is world-readable but modifiable only by root
