# Create a Satellite host errata report (csv)

To get a frequently report of installable Red Hat errata on a per host basis you can use this Python script. Download it to your Satellite server or any other host where Python 2.7 is installed.

### Table of Contents
- [Prerequisites](#Prerequisites)
- [1. Where to get the available API calls](#1.%20Where%20to%20get%20the%20available%20API%20calls)


## Prerequisites
Once you`ve cloned the Git repo open the Python script host_errata_report.py and fill in the following variables:

- URL
- USERNAME
- ORG_NAME
- crypted_password
- key

> You can get these values for the last two variables from the crypt.py script described in chapter 4.

## 1.  Where to get the available API calls

You can find all available API calls on your Satellite server:

https://satellite.example.com/apidoc/v2.html

## 2. Where to find the available JSON fields to query within the Python script?

To get an overview about all available JSON fields you can run an API call via Curl on the Satellite server to e. g. list all available errata for a given host:

```
curl -X GET -s -k -u <user>:<password> https://satellite.example.com/api/hosts/host01.example.com/errata?per_page=5000 | python -m json.tool
```

This gives you the following list:
```
{
    "error": null,
    "page": 1,
    "per_page": "5000",
    "results": [
        {
            "bugs": [
                {
                    "bug_id": "1813091",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1813091"
                },
                {
                    "bug_id": "1813758",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1813758"
                }
            ],
            "cves": [],
            "description": "Red Hat OpenStack Platform provides the facilities for building, deploying\nand monitoring a private or public infrastructure-as-a-service (IaaS) cloud\nrunning on commonly available physical hardware.\n\nChanges to the openstack-tripleo-heat-templates component:\n\n* Before this update, when upgrading Red Hat OpenStack Platform (RHOSP) 13 on 64-bit PowerPC processors to the latest maintenance release, Paunch would fail to create the `nova_libvirt` container, report the following error, and cause the upgrade to fail:\n\n /usr/bin/docker-current: Error response from daemon:\n Requested CPUs are not available\u2026.\n\nThe value of the RHOSP parameter, `cpuset_cpus`, in nova-libvirt.yaml defaults to all CPUs. In cases where the simultaneous multithreading (SMT) control was disabled, the CPUs were exposed differently and the RHOSP upgrade was failing.\n\nTwo changes have been made to resolve this issue. First, by default, Docker automatically determines for you which CPUs are available. The second change is that you can use a new role-based parameter, `ContainerCpusetCpus` to override Docker. For more information, see https://access.redhat.com/solutions/4917021. (BZ#1813091)",
            "errata_id": "RHBA-2020:1297",
            "hosts_applicable_count": 11,
            "hosts_available_count": 11,
            "id": 6949,
            "installable": true,
            "issued": "2020-04-02",
            "module_streams": [],
            "name": "Red Hat OpenStack Platform 13.0 director bug fix advisory",
            "packages": [
                "openstack-tripleo-common-8.7.1-15.el7ost.noarch",
                "openstack-tripleo-common-container-base-8.7.1-15.el7ost.noarch",
                "openstack-tripleo-common-containers-8.7.1-15.el7ost.noarch",
                "openstack-tripleo-common-devtools-8.7.1-15.el7ost.noarch",
                "openstack-tripleo-heat-templates-8.4.1-51.el7ost.noarch",
                "python-paunch-2.5.3-3.el7ost.noarch"
            ],
            "pulp_id": "c704b752-78c4-47c1-9497-eeb05c6a649a",
            "reboot_suggested": false,
            "severity": "None",
            "solution": "Before applying this update, ensure all previously released errata relevant\nto your system have been applied.\n\nRed Hat OpenStack Platform 13 runs on Red Hat Enterprise Linux 7.7.\n\nThe Red Hat OpenStack Platform 13 Release Notes contain the following:\n* An explanation of the way in which the provided components interact to\nform a working cloud computing environment.\n* Technology Previews, Recommended Practices, and Known Issues.\n* The channels required for Red Hat OpenStack Platform 13, including which\nchannels need to be enabled and disabled.\n\nThe Release Notes are available at:\nhttps://access.redhat.com/documentation/en-us/red_hat_openstack_platform/13/html/release_notes/\n\nThis update is available through 'yum update' on systems registered through\nRed Hat Subscription Manager. For more information about Red Hat\nSubscription Manager, see:\n\nhttps://access.redhat.com/documentation/en-US/Red_Hat_Subscription_Management/1/html/RHSM/index.html",
            "summary": "Updated director installer packages that resolve various issues are now\navailable for Red Hat OpenStack Platform 13.0 (Queens) for RHEL 7.",
            "title": "Red Hat OpenStack Platform 13.0 director bug fix advisory",
            "type": "bugfix",
            "updated": "2020-04-02",
            "uuid": "c704b752-78c4-47c1-9497-eeb05c6a649a"
        },
        {
            "bugs": [
                {
                    "bug_id": "1769895",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1769895"
                }
            ],
            "cves": [],
            "description": "Red Hat Satellite is a system management solution that allows organizations to configure and maintain their systems without the necessity to provide public Internet access to their servers or other client systems. It performs provisioning and configuration management of predefined standard operating environments.\n\nThis update fixes the following bug: \n\n* There was a problem causing memory leakage from qpid-proton. (BZ#1769895)\n\nUsers of Red Hat Satellite Tools on all Red Hat Enterprise Linux versions are advised to upgrade to these updated packages.",
            "errata_id": "RHBA-2019:4105",
            "hosts_applicable_count": 11,
            "hosts_available_count": 11,
            "id": 6718,
            "installable": true,
            "issued": "2019-12-04",
            "module_streams": [],
            "name": "Satellite Tools 6.6.1 Async Bug Fix Update",
            "packages": [
                "foreman-cli-1.22.0.33-1.el7sat.noarch",
                "python3-qpid-proton-0.28.0-2.el8.x86_64",
                "python-qpid-proton-0.28.0-2.el7.x86_64",
                "qpid-proton-c-0.28.0-2.el7.x86_64",
                "qpid-proton-c-0.28.0-2.el8.x86_64",
                "satellite-cli-6.6.1-1.el7sat.noarch"
            ],
            "pulp_id": "3c7060a9-eb85-40ad-811e-49bf7a07f581",
            "reboot_suggested": false,
            "severity": "None",
            "solution": "Before applying this update, make sure all previously released errata relevant to your system have been applied.\n\nFor details on how to apply this update, refer to:\n\nhttps://access.redhat.com/articles/11258",
            "summary": "Updated Satellite 6.6 Tools packages that fix several bugs are now available.",
            "title": "Satellite Tools 6.6.1 Async Bug Fix Update",
            "type": "bugfix",
            "updated": "2019-12-04",
            "uuid": "3c7060a9-eb85-40ad-811e-49bf7a07f581"
        },
        {
            "bugs": [
                {
                    "bug_id": "1686493",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1686493"
                },
                {
                    "bug_id": "1706427",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1706427"
                },
                {
                    "bug_id": "1713222",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1713222"
                },
                {
                    "bug_id": "1716294",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1716294"
                },
                {
                    "bug_id": "1730026",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1730026"
                },
                {
                    "bug_id": "1731746",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1731746"
                },
                {
                    "bug_id": "1738893",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1738893"
                },
                {
                    "bug_id": "1743156",
                    "href": "https://bugzilla.redhat.com/show_bug.cgi?id=1743156"
                }
            ],
            "cves": [],
            "description": "Red Hat Satellite is a systems management tool for Linux-based infrastructure. It allows for provisioning, remote management, and monitoring of multiple Linux deployments with a single centralized tool.\n\nThis update provides the Satellite 6.6 Tools repositories. For the full list of new features provided by Satellite 6.6, see the Release Notes linked to in the references section. See the Satellite 6 Installation Guide for detailed instructions on how to install a new Satellite 6.6 environment, or the Satellite 6 Upgrading and Updating guide for detailed instructions on how to upgrade from prior versions of Satellite 6.\n\nThis update fixes the following bugs: \n\n* The Hammer hostgroup command now has a 'rebuild_config' argument that you can use to rebuild host group configurations. (BZ#1686493)\n* Installing the Katello agent on Red Hat Enterprise Linux 6 was failing with the following error: python-pulp-common requires python2-isodate. (BZ#1706427)\n* The Hammer hostgroup command had a problem with the '--environment' option that caused host group creation to fail. (BZ#1713222)\n* Although hosts were successfully created, Hammer displayed the following error: Could not create the host. (BZ#1716294)\n* Some Hammer docker commands were failing with the following error: Error: uninitialized constant HammerCLIKatello::LifecycleEnvironmentNameResolvable. (BZ#1730026)\n* The Hammer docker commands' error messages did not provide enough information. (BZ#1731746)\n* Updating the Katello agent did not update the gofer package. (BZ#1738893)\n* An error was introduced that prevented hosts from being created. (BZ#1743156)\n* Updates introduced to support fixes for qpid-proton: TLS Man in the Middle Vulnerability (CVE-2019-0223) for Satellite Tools. (BZ#1749547)\n\nAll users who require Satellite version 6.6 are advised to install these new packages.",
            "errata_id": "RHBA-2019:3175",
            "hosts_applicable_count": 14,
            "hosts_available_count": 14,
            "id": 6717,
            "installable": true,
            "issued": "2019-10-22",
            "module_streams": [],
            "name": "Satellite 6.6 Tools Release",
            "packages": [
                "foreman-cli-1.22.0.32-1.el7sat.noarch",
                "gofer-2.12.5-5.el7sat.noarch",
                "gofer-2.12.5-5.el8sat.noarch",
                "katello-agent-3.5.1-2.el7sat.noarch",
                "katello-agent-3.5.1-2.el8sat.noarch",
                "katello-host-tools-3.5.1-2.el7sat.noarch",
                "katello-host-tools-3.5.1-2.el8sat.noarch",
                "katello-host-tools-fact-plugin-3.5.1-2.el7sat.noarch",
                "katello-host-tools-tracer-3.5.1-2.el7sat.noarch",
                "katello-host-tools-tracer-3.5.1-2.el8sat.noarch",
                "pulp-puppet-tools-2.19.1-2.el7sat.noarch",
                "puppet-agent-5.5.12-1.el7sat.x86_64",
                "puppet-agent-5.5.12-1.el8sat.x86_64",
                "python2-beautifulsoup4-4.6.3-2.el7sat.noarch",
                "python2-future-0.16.0-11.el7sat.noarch",
                "python2-gofer-2.12.5-5.el8sat.noarch",
                "python2-isodate-0.5.4-12.el7sat.noarch",
                "python2-tracer-0.7.1-2.el7sat.noarch",
                "python3-beautifulsoup4-4.6.3-2.el8sat.noarch",
                "python3-future-0.16.0-11.el8sat.noarch",
                "python3-gofer-2.12.5-5.el8sat.noarch",
                "python3-gofer-proton-2.12.5-5.el8sat.noarch",
                "python3-qpid-proton-0.28.0-1.el8.x86_64",
                "python3-tracer-0.7.1-2.el8sat.noarch",
                "python-argcomplete-1.7.0-2.el7sat.noarch",
                "python-gofer-2.12.5-5.el7sat.noarch",
                "python-gofer-proton-2.12.5-5.el7sat.noarch",
                "python-psutil-5.0.1-3.el7sat.x86_64",
                "python-pulp-common-2.19.1.1-1.el7sat.noarch",
                "python-pulp-manifest-2.19.1.1-2.el7sat.noarch",
                "python-pulp-puppet-common-2.19.1-2.el7sat.noarch",
                "python-qpid-proton-0.28.0-1.el7.x86_64",
                "qpid-proton-c-0.28.0-1.el7.x86_64",
                "qpid-proton-c-0.28.0-1.el8.x86_64",
                "rubygem-foreman_scap_client-0.4.6-1.el7sat.noarch",
                "rubygem-foreman_scap_client-0.4.6-1.el8sat.noarch",
                "satellite-cli-6.6.0-7.el7sat.noarch",
                "tfm-ror52-rubygem-mime-types-3.2.2-1.el7sat.noarch",
                "tfm-ror52-rubygem-mime-types-data-3.2018.0812-1.el7sat.noarch",
                "tfm-ror52-rubygem-multi_json-1.13.1-1.el7sat.noarch",
                "tfm-ror52-runtime-1.0-4.el7sat.x86_64",
                "tfm-rubygem-apipie-bindings-0.2.2-2.el7sat.noarch",
                "tfm-rubygem-awesome_print-1.8.0-3.el7sat.noarch",
                "tfm-rubygem-clamp-1.1.2-5.el7sat.noarch",
                "tfm-rubygem-domain_name-0.5.20160310-4.el7sat.noarch",
                "tfm-rubygem-fast_gettext-1.4.1-3.el7sat.noarch",
                "tfm-rubygem-hammer_cli-0.17.1-2.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman-0.17.0.8-1.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_admin-0.0.8-3.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_ansible-0.3.2-1.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_bootdisk-0.1.3.3-5.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_discovery-1.0.1-1.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_docker-0.0.6.4-1.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_openscap-0.1.7-2.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_remote_execution-0.1.0-3.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_tasks-0.0.13-2.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_templates-0.1.2-2.el7sat.noarch",
                "tfm-rubygem-hammer_cli_foreman_virt_who_configure-0.0.4-1.el7sat.noarch",
                "tfm-rubygem-hammer_cli_katello-0.18.0.6-1.el7sat.noarch",
                "tfm-rubygem-hashie-3.6.0-1.el7sat.noarch",
                "tfm-rubygem-highline-1.7.8-4.el7sat.noarch",
                "tfm-rubygem-http-cookie-1.0.2-5.el7sat.noarch",
                "tfm-rubygem-little-plugger-1.1.3-24.el7sat.noarch",
                "tfm-rubygem-locale-2.0.9-13.el7sat.noarch",
                "tfm-rubygem-logging-2.2.2-5.el7sat.noarch",
                "tfm-rubygem-netrc-0.11.0-3.el7sat.noarch",
                "tfm-rubygem-oauth-0.5.4-3.el7sat.noarch",
                "tfm-rubygem-powerbar-2.0.1-2.el7sat.noarch",
                "tfm-rubygem-rest-client-2.0.1-4.el7sat.noarch",
                "tfm-rubygem-unf-0.1.3-7.el7sat.noarch",
                "tfm-rubygem-unf_ext-0.0.6-9.el7sat.x86_64",
                "tfm-rubygem-unicode-0.4.4.1-6.el7sat.x86_64",
                "tfm-rubygem-unicode-display_width-1.0.5-5.el7sat.noarch",
                "tfm-runtime-5.0-7.el7sat.x86_64",
                "tracer-common-0.7.1-2.el7sat.noarch",
                "tracer-common-0.7.1-2.el8sat.noarch"
            ],
            "pulp_id": "1af9f9eb-658a-4f24-9d4e-62bdf7cd2f96",
            "reboot_suggested": false,
            "severity": "None",
            "solution": "Before applying this update, make sure all previously released errata\nrelevant to your system have been applied.\n\nFor details on how to apply this update, refer to:\n\nhttps://access.redhat.com/articles/11258",
            "summary": "An update is now available for Satellite Tools 6.6.",
            "title": "Satellite 6.6 Tools Release",
            "type": "bugfix",
            "updated": "2019-10-22",
            "uuid": "1af9f9eb-658a-4f24-9d4e-62bdf7cd2f96"
        }
    ],
    "search": null,
    "sort": {
        "by": "updated",
        "order": "desc"
    },
    "subtotal": 3,
    "total": 3
}
```

Here you can see three available Errata for the host host01.example.com. Within the Python script you can see that the key fields of the JSON output is searchable. In the main() function you can see for example that in the “for” loop the "Errata ID: " + (erratum['errata_id'])” will be printed. The key “errata_id” is also shown in the output above

You can also iterate through nested JSON. If you for example want to get host information with 

```
curl -X GET -s -k -u user:password https://satellite.example.com/api/hosts/host01.example.com | python -m json.tool
```

This gives you the following output:
```
{
    "all_parameters": [
        {
            "created_at": "2019-08-30 10:36:18 UTC",
            "id": 2,
            "name": "enable-puppet5",
            "parameter_type": null,
            "priority": 0,
            "updated_at": "2019-08-30 10:36:18 UTC",
            "value": "true"
        },
        {
            "created_at": "2019-08-30 10:36:18 UTC",
            "id": 1,
            "name": "enable-epel",
            "parameter_type": null,
            "priority": 0,
            "updated_at": "2019-08-30 10:36:18 UTC",
            "value": "false"
        }
    ],
    "all_puppetclasses": [],
    "architecture_id": 1,
    "architecture_name": "x86_64",
    "build": false,
    "capabilities": [
        "build"
    ],
    "certname": "host01.example.com",
    "comment": "",
    "compute_profile_id": null,
    "compute_profile_name": null,
    "compute_resource_id": null,
    "compute_resource_name": null,
    "config_groups": [],
    "content_facet_attributes": {
        "applicable_module_stream_count": 0,
        "applicable_package_count": 188,
        "content_source": null,
        "content_source_id": null,
        "content_source_name": null,
        "content_view": {
            "id": 27,
            "name": "cv_rhel7"
        },
        "content_view_default?": false,
        "content_view_id": 27,
        "content_view_name": "cv_rhel7",
        "content_view_version": "4.0",
        "content_view_version_id": 151,
        "errata_counts": {
            "bugfix": 39,
            "enhancement": 3,
            "security": 17,
            "total": 59
        },
[...]
```

We are interested in the key:value 

```
"content_facet_attributes"
	→ "errata_counts"
		→ "total"
```

which gives us a hint if installable errata for this host are available. So in the Python script we use `host['content_facet_attributes']['errata_counts']['total']` within the for-loop to access exactly this data.

## 3 Where can I find the generated csv report file?

The script stores the generated report file in csv format under `errata_report-' + current_date + '.csv'`. You can simply format the data as “table” and filter each column as needed.

## 4 Using encrypted Satellite user password in the Python script

To not store a plaintext user password in the Python script, even if the script is stored in /root home directory and has the access right 700, you should encrypt the user password you use to connect to the Satellite API within the Python script.

Therefore the module `sha256_crypt from passlib.hash` as well as `Fernet from cryptography.fernet` are used to decrypt the users password.

To crypt the Satellite user password you can use the `crypt.py` script. Open it and store your Satellite user password in the variable "password". Then run the script. It will print out the used Fernet key and the encrypted password. 

Copy the key and the encrypted password and store these information in the host_errata_report.py script. The variables are 
- crypted_password
- key

> Please ensure that you remove the unencrypted password from the variable "password" in the crypt.py script once you have the encrypted password and key available.
> Of course this is not very secure because you know the key which was used to encrypt the user password. But for an inexperienced Python developer this is not obvious and he just sees an encrypted password.
