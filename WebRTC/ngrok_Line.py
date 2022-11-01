from pyngrok import ngrok

token = "2FM9hVmFjGxvAQLtqhzUouXBvMB_35eUbpExjAaERX4Rr7Bh2"


ngrok.set_auth_token(token)
http_tunnel = ngrok.connect(addr = 5000, scheme = True)
print(http_tunnel.public_url)

