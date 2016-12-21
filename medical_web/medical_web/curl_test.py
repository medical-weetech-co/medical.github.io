'''
curl -XPOST -d "username=jason&password=" http://localhost:8001/api/auth/token/

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InBlaWNoaWVoQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiamFzb24iLCJ1c2VyX2lkIjoxLCJleHAiOjE0ODIzMDg4MTh9.jz8gRzN83PiPkZnXj_VyjF1312SqFYgxKWwNvyym3jI

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InBlaWNoaWVoQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiamFzb24iLCJ1c2VyX2lkIjoxLCJleHAiOjE0ODIzMDg4MTh9.jz8gRzN83PiPkZnXj_VyjF1312SqFYgxKWwNvyym3jI" http://localhost:8001/api/comments/

curl -XPOST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imphc29uIiwiZW1haWwiOiJwZWljaGllaEBnbWFpbC5jb20iLCJleHAiOjE0ODIzMDk4MDR9._uBN5RIcmP-D_vecyBnf98TYeGZUF4-A8S4PflorWAs" -H "Content-Type: application/json" -d '{"content": "some reply"}' 'http://localhost:8001/api/comments/create/?type=post&slug=new-title&parent_id=26'

'''