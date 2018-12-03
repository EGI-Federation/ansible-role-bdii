# BDII

[![Build Status](https://travis-ci.org/EGI-Foundation/ansible-role-bdii.svg?branch=master)](https://travis-ci.org/EGI-Foundation/ansible-role-bdii)

<!-- A brief description of the role goes here. -->
This role is for deploying the Berkeley Database Information Index
(BDII), specifically for providing a common information schema
in distributed computing infrastructures.

This role can deliver all levels of the BDII:

- top-bdii (combination of many site-bdiis)
- site-bdii (combination of many resource bdiis)
- resource-bdii (single resource information index)

## Requirements

No explicit requirements.

## Role Variables

The main role variables are in `defaults/main.yml`, while the bdii-specific
vars are in `defaults/bdii.yml`.
Overwrite these with your own vars in your group vars, or add your own to `vars/main.yml`


## Dependencies

<!--
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Use https://galaxy.ansible.com/EGI-Foundation/ roles first if possible.
-->

This role depends on the [umd role](https://github.com/EGI-Foundation/ansible-role-umd) from EGI Foundation.
This role ensures that the UMD base distribution is installed and the repositories configured.


## Example Playbook

<!--
Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:
-->

```yaml
    - hosts: servers
      roles:
         - { role: egi-foundation.umd4, umd_version: 4 }
         - { role: egi-foundation.bdii, level: top }
```

## Testing

Molecule is used to test the various scenarios.
Test scenarios are found in the `molecule/` directory.
Current test scenarios include:

- top-bdii:
  - Docker
  - VirtualBox with Vagrant
- site-bdii:
  - Docker
- default
  - docker

## License

Apache-2.0

## Author Information

[Bruce Becker](@brucellino), and others.
<!--
Add the relevant contributors
-->