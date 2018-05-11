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

None

## Role Variables

The main role variables are in `defaults/main.yml`, while the bdii-specific
vars are in `defaults/bdii.yml`.
Overwrite these with your own vars in your group vars, or add your own to `vars/main.yml`

## Dependencies

<!--
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Use https://galaxy.ansible.com/EGI-Foundation/ roles first if possible.
-->

See `meta.yml` for dependencies.

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

[Bruce Becker](@brucellino), and others.
<!--
Add the relevant contributors
-->