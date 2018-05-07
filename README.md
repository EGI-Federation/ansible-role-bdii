[![Build Status](https://travis-ci.org/EGI-Foundation/ansible-umd-bdii-role.svg?branch=master)](https://travis-ci.org/EGI-Foundation/ansible-umd-bdii-role)

# BDII

<!-- A brief description of the role goes here. -->
This role is for deploying the Berkeley Database Information Index
(BDII), specifically for providing a common information schema
in distributed computing infrastructures.

This role can deliver all levels of the BDII:

- top-bdii (combination of many site-bdiis)
- site-bdii (combination of many resource bdiis)
- resource-bdii (single resource information index)

## Requirements

<!--
Any pre-requisites that may not be covered by Ansible itself or the role should be
mentioned here.
For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
-->
None

## Role Variables

<!--
A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.
-->
The main role variables are in `vars/main.ym`, while the bdii-level-specific
vars are in the relevant file in `vars/` and  `defaults/` _etc_:

- `vars/top.yml` - vars necessary to deliver _your_ top-bdii
- `vars/site.yml` - vars necessary to deliver _your_ site-bdii
- `vars/resource.yml` - vars necessary to deliver  a site resource (e.g. compute endpoint)

## Dependencies

<!--
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Use https://galaxy.ansible.com/EGI-Foundation/ roles first if possible.
-->

## Example Playbook

<!--
Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:
-->

```yaml
    - hosts: servers
      roles:
         - { role: EGI-Foundation.umd-bdii, level: top, umd_version: 4 }
```

## License

Apache-2.0

## Author Information

<!--
Add the relevant contributors
-->