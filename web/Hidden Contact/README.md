# Hidden Contact
==============
Author: [Pran-Ker](https://github.com/Pran-Ker)

## Description
---------------
Finding the site database password. We all know you can't .

## Requirements
--------------

- docker-compose

## Sources
------------

Copy the whole folder contents to, for instance, `/opt/ctf/w100/`.
Then you need to configure Wordpress to accept requests on the virtual host you desire. For that replace any reference to `localhost:30100` in the `sql/wordpress.sql` file with the new virtual host, for instance using `sed 's/localhost:9999/newhostname/g' sql/wordpress.sql`

Then you just need to link the systemd service with `sudo ln -s /opt/ctf/w100/w100.service /etc/systemd/system/w100.service` and start it with `sudo systemdctl start w100.service`.By default it will listen in the `9999` port.



## Exploit
---------

By visiting the site you can easily recognize as a Wordpress blog. This might distract you and lead you to thinking the way to go is through `/wp-login`, `/wp-admin` or the `xml-rpc` interface. But this is an up-to-date version of Wordpress (it was, when it was used in the CTF) and the challenge question clearly talks about admin skills.

A quick visit to the Wordpress well-known paths, present in any installation, will reveal a directory listing at `/wp-content/plugins`, which is, coincidently, a common source of problems. 

You immediately notice a `upload.html` file that lets you upload files, without content or file extension restrictions and prints back where the file was copied to, right into the document root.

You just need to upload a PHP file that reads the `wp-config.php` file and read the contents of the `DB_PASSWORD` variable. You can easily do that with this file:

```
<?php
echo file_get_contents("../../wp-config.php");
?>
```

Then just visit the file you have uploaded, something like `/wp-contents/plugin/../../uploads/hiden_<random_id1>/<random_id2>.php` and view the source of the page.


## Flag
----

csictf{c0nt4ct_m3_0nc3_ur_d0n3}
