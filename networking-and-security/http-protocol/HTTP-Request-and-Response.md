We can learn a lot by taking a closer look on a raw HTTP request and response that sent over the network:
```bash
curl -v http://httpbin.org/html
```
Below is the actual raw HTTP request sent by `curl` to the server:
```bash
GET /html HTTP/1.1
Host: httpbin.org
User-Agent: curl/7.58.0
Accept: */*
```
The server response is:
```bash
HTTP/1.1 200 OK
Date: Wed, 05 Apr 2023 12:43:42 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3741
Connection: keep-alive
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

<!DOCTYPE html>
<html>
  <head>
....
```
The MDN web docs [specify the core components of request and response objects](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#http_flow), review this resource.

**Status code**
HTTP response status codes indicate how a specific HTTP request was completed.

Responses are grouped in five classes:
1. Informational (100–199)
1. Successful (200–299)
1. Redirection (300–399)
1. Client error (400–499)
1. Server error (500–599)

Try yourself to perform the below two HTTP requests, and read about the meaning of each status code.
```bash
curl -i httpbin.org/status/0
curl -v -X PUT httpbin.org/path/to/nowhere
```