# effective-pancake
A teaching tool for web application security

**THIS CONTAINS DELIBERATELY INSECURE CODE**

**DO NOT USE THIS CODE FOR ANYTHING, EVER**

## What is this nonsense?

Inspired by [Joe's Bacon Emporium](https://github.com/devjack/joes-bacon-emporium), this is a simple web application written in [Flask](http://flask.pocoo.org/) which contains several significant securitiy vulnerabilities.

Despite using some apparent best practices, it is possible for an unauthenticated user to exploit vulnerabilities in this application and the webserver configuration to gain root on the hosting box. For this reason, the application runs in a vagrant container.

This is intended as a teaching tool. It's called effective-pancake because that's what Github suggested.

## Cheating

The VULNERABILITIES.md file contains a list of known vulnerabilities. There may be unknown vulnerabilities as well!

This file is designed for use by the instructor of a workshop. It does not contain a detailed explanation of the vulnerabilities, but points to where the vulnerabilities occur. If you want more information on any of them, you can [contact me](https://mjec.net).

## Getting up and running

1. Install [Vagrant](https://www.vagrantup.com/) using your preferred mechanism.

2. Run `git clone https://github.com/mjec/effective-pancake.git` in a local directory.

3. Run `cd effective-pancake` and then `vagrant up` to start the box.

By default this will serve on `http://127.0.0.1:8080/`. You can modify this port in the `Vagrantfile`.

