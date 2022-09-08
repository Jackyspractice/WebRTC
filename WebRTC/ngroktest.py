from pyngrok import ngrok

token = "2EFlxQQDpreqVGMuQVTtTepMzHB_7Px3VmMDjcQxgLoDH7Ync"


ngrok.set_auth_token(token)
http_tunnel = ngrok.connect(8080)
print(http_tunnel.public_url)

