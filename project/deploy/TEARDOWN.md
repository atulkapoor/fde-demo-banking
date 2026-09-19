# Taking it away

## The application

The substrate has no concept of un-doing, so these are manual and written out rather than left implied.

```bash
sudo systemctl disable --now app
sudo rm /etc/systemd/system/app.service
sudo systemctl daemon-reload
sudo rm -rf /opt/app /var/lib/app
sudo userdel app
```

## The environment

```bash
cd deploy/terraform
terraform destroy
```

This tool tracks what it created, so this takes it away cleanly. Check that no state remains in a remote backend afterwards.

Then confirm nothing was left behind: data directories, secrets in a vault, DNS entries, and anything created by hand during the engagement.
