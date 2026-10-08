Name:           oobasename
Version:        0.2.0
Release:        1%{?dist}
Summary:        Strips directory prefixes and optional file extensions from path strings.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobasename
Source0:        oobasename-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobasename is a sovereign, capability-bounded FILENAME STRIPPER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobasename
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobasename-uninstall

%files
/usr/bin/oobasename
/usr/bin/oobasename-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevated to v0.2.0 with pure native openOODA, multiple-path support, suffix stripping, and MCP server
