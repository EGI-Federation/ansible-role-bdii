import os
# import requests
# import xml.etree.ElementTree
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
# site = requests.get('https://goc.egi.eu/gocdbpi/public/
# ?method=get_site&sitename=ZA-MERAKA')


def test_slapd_user(host):
    user = host.user('ldap')

    assert user.exists
    assert user.shell == '/usr/sbin/nologin'


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_config_files(host):
    bdii_conf = host.file('/etc/bdii/bdii.conf')
    bdii_sysconfig = host.file('/etc/sysconfig/bdii')
    bdii_site_config_file = host.file('/etc/glite-info-static/site/site.cfg')
    bdii_slapd_config_file = host.file('/etc/bdii-slapd.conf')

    assert bdii_conf.exists
    assert bdii_conf.is_file
    assert bdii_conf.user == 'root'

    assert bdii_sysconfig.exists
    assert bdii_sysconfig.is_file
    assert bdii_sysconfig.user == 'root'
    assert bdii_sysconfig.contains('^SLAPD_CONF = .*')
    assert bdii_sysconfig.contains('SLAPD=/usr/sbin/slapd')

    assert bdii_site_config_file.exists
    assert bdii_site_config_file.is_file
    assert bdii_site_config_file.user == 'root'

    assert bdii_slapd_config_file.exists
    assert bdii_slapd_config_file.is_file
    assert bdii_slapd_config_file.user == 'ldap'
    assert not bdii_slapd_config_file.contains('not_set')


def test_log_files(host):
    bdii_log_dir = host.file('/var/log/bdii')

    assert bdii_log_dir.exists
    assert bdii_log_dir.is_directory
    assert bdii_log_dir.user == 'ldap'


def test_data_files(host):
    data_dir = host.file('/var/lib/bdii')

    assert data_dir.exists
    assert data_dir.is_directory
    assert data_dir.user == 'ldap'
