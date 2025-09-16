# Exercise 1 - Accept Header
Use curl to perform an HTTP GET request to `http://httpbin.org/image`. Add an Accept header to your requests to indicate to the server that you anticipate a png  image. Read carefully the Warning message written by curl at the end of the server response, follow the instructions to save the image on the file system. Execute another curl to save the image in the file system. Which animal appears in the served image?
<details>
  <summary>
    Solution
  </summary>

```bash
curl -i -H "Accept: image/png" http://httpbin.org/image
curl -i -H "Accept: image/png" --output image.png http://httpbin.org/image
```
Notes:
 
The -i option (--include) includes the HTTP response headers in the output (while -v includes both request and response headers as well as additional debug info).

</details>

# Exercise 2 - Status Code
1. Perform an HTTP GET request to google.com
1. What does the server response status code mean? Follow the response headers and body to get the real Google's home page.
1. Which HTTP version does the server use in the above response?
<details>
  <summary>
    Solution
  </summary>

1. curl -i google.com
1. curl -i https://www.google.com
1. HTTP/2

</details>

# Exercise 3 - Connection Close
The server of `http://httpbin.org` uses `keep-alive` connection by default, indicating that the server would like to keep the TCP connection open, so further requests to the server will use the same underlying TCP socket.

Perform an HTTP POST request to the `/anything` endpoint and tell the server that the client (you) would like to close the connection immediately after the server has responded.

Make sure the server's response contains the `Connection: close` header which means that the TCP connection used to serve the request was closed.  
<details>
  <summary>
    Solution
  </summary>

```bash
 curl -i -X POST -H "Connection: close" 
 http://httpbin.org/anything
```

</details>

# Exercise 4 - Sending Data to the Server
Perform an HTTP POST request to `http://httpbin.org/anything`. You should send the following json to the server
```bash
{"test": "me"}
```
Upon success request, the response body will be a json format with a "json" key and your data as a value, as follows:
```bash
"json": {
  "test": "me"
}
```
Bad requests would be responded to by:
```bash
"json": null
```
<details>
  <summary>
    Solution
  </summary>

```bash
 curl -i -X POST -H "Content-Type: application/json" -d '{"test": "me"}' http://httpbin.org/anything
 ```

</details>

# Exercise 5 - Set Cookie
Using `curl`, perform an HTTP GET request to `http://httpbin.org/cookies/set`, while adding the following query parameters to the URL:
- color-theme=light
- visitor-id=59201456801
- lang=en

Query parameters is the set of key-value pairs that go after the ? in a URL, separated by & characters.

e.g.:
```bash
http://127.0.0.1:8000/some/endpoint?k1=value1&k2=value2
```
The `/cookies/set` is a designated endpoint that will add `Set-Cookie` headers according to the specified URL query parameters. Use the `--cookie-jar my-cookies.txt` option in order to save the cookies in the file `my-cookies.txt`.
<details>
  <summary>
    Solution
  </summary>

```bash
curl -i --cookie-jar my-cookies.txt "httpbin.org/cookies/set?color-theme=light&visitor-id=59201456801&lang=en"
```

</details>

# Exercise 6 - Send a Cookie
By default, your browser will send cookies to the corresponding servers. We will use `curl` with the option `--cookie my-cookies.txt` to send cookies to the server. Perform an HTTP GET request to `http://httpbin.org/cookies`. Use the `-v` option to see how the `Cookie` header was set in the request. Upon success, the server response body-entity should be:
```bash
{
  "cookies": {
	"color-theme": "light",
	"lang": "en",
	"visitor-id": "59201456801"
  }
}
```
`Note`: It is uncommon for a server to attach the user cookies in the response body. Keep in mind that `httpbin.org` is a toy server that helps you learn the HTTP protocol. The /cookies endpoint was designed specifically to respond with your cookies for debugging purposes.

# Exercise 7 - Experimenting with APIs
Use Postman to retrieve data from some interesting free API:

https://github.com/public-apis/public-apis