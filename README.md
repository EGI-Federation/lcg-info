# lcg-info

This command line tool allows the user to query the WLCG/EGI, LDAP-based
information system.

BDII documentation is available with the main [BDII
documentation](https://gridinfo-documentation.readthedocs.io/)

## Usage

This program requires the environmental variable `LCG_GFAL_INFOSYS`, or the
`--bdii option`, to be set to a comma-separated list of BDII endpoints to be
interrogated, e.g. `mybdii.domain.org:2170`. All BDII endpoints in the list are
queried until one answers.

```sh
lcg-info --list-ce [--bdii bdii] [--vo vo] [--sed] [--debug]
         [--query query] [--attrs list]

lcg-info --list-se [--bdii bdii] [--vo vo] [--sed] [--debug]
         [--query query] [--attrs list]

lcg-info --list-service [--bdii bdii] [--vo vo] [--sed] [--debug]
         [--query query] [--attrs list]

lcg-info --list-site [--bdii bdii] [--vo vo] [--sed] [--debug]
         [--query query] [--attrs list]

lcg-info --list-attrs

lcg-info --help
```

### Example

```sh
lcg-info --list-se --vo ops --attrs SESite --bdii bdii.fqdn.tld:2170
```

## Installing from source

This procedure is not recommended for production deployment, please consider
using packages.

Get the source by cloning this repository and doing a `make install`.

perl-LDAP is required.

## Building packages

A Makefile allowing to build source tarball and packages is provided.

### Building a RPM

The required build dependencies are:

- rpm-build
- make
- rsync

The required runtime dependency is:

- perl-LDAP

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Foundation/lcg-info.git
cd lcg-info
git checkout X.X.X
# Building in a container
docker run --rm -v $(pwd):/source -it centos:7
yum install -y rpm-build make rsync gcc
yum-builddep -y lcg-info.spec
cd /source && make rpm
```

The RPM will be available into the `build/RPMS` directory.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR including
  - Update of version and changelog in `lcg-info.spec`
  - Update of version and changelog in `debian/changelog`
  - Update of authors in `AUTHORS`
- Once the PR has been merged draft a new release from master in GitHub
  - using the vX.X.X format for the tag version
  - using the X.X.X for the release title
  - adding changelog in the description
  - Publish the release

Packages will be built using Travis and attached to the release page.

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN.
This is now hosted here on GitHub, maintained by the BDII community with
support of members of the EGI Federation.
