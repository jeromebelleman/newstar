# NAME

newstar – Nova shell

# DESCRIPTION

This CLI allows you to manage OpenStack VMs and attempts to make tenants
transparent by keeping a mapping between VMs and their tenants. You may then
query information about or perform operations on VMs without having to care
about which tenant they belong to.

This tool is brutal. It aims at speeding up communication with the OpenStack
service by running queries in parallel. You may want to use it sparingly.

# SETUP

Running the **newstar** command will create the **~/.newstar** directory
where it will keep command output pages and command history. In addition
to this it will expect to find the **~/.newstar/newstar.yaml** file where
OpenStack tenants and **newstar** settings are to be defined. For instance:

```
services:
    corge:
        url:    https://openstack.example.net:5000/v2.0
        tenants:
            - id:     01234567-89ab-cdef-0123-456789abcdef
              name:   Foo

            - id:     1234567-89ab-cdef-0123-456789abcdef0
              name:   Bar

            - id:     234567-89ab-cdef-0123-456789abcdef01
              name:   Baz

threads:
    vm:         16 # 16 seems to be the optimal balance
    tenant:     16 # Should be more than the number of tenants
```

The **threads** section specifies the number of threads which should be
querying the OpenStack service for VM information (**vm**) and VM lists
(**list**).

If they have been installed on your system, **newstar** symbolic links of
the form **newstar-foo** will instead use the **/etc/newstar/foo.yaml**
configuration file.

# COMMANDS

Starting **newstar** without options will launch the shell. The available
commands can be displayed with the **help** (or **?**) command.

The **list** command lists VMs which have been found in the different tenants
specified in the configuration file. It also updates the tenant-VM mappings
everywhere.  The **lstenants** command lists the known tenants. The **limits**
command lists quota and usage in all known tenants. The **show**, **reboot**,
**remove**, **console** and **chown** commands use the mappings populated
by **list**. If they cannot find any of the specified VMs, you might need
to run **list** again.

The **edit** command lets you edit a command line with Vim.  The **page**
command pages in Vim the output of the last **show**, **list** or **console**
commands.
