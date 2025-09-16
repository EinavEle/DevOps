In order to get data over the network, lots of different hardware and software need to work and communicate together via a well-defined **protocol**. A protocol is, simply put, a set of rules for communication. You know some of them: HTTP, SSH, TCP/IP etc... All these different types of communication protocols are classified in 7 layers, which are known as the Open Systems Interconnection Reference Model, the OSI Model for short.

In this course we will discuss the 4-layer model, which is a simplified version of the OSI model that combines several of the OSI layers into four layers.

This model is commonly used in the TCP/IP protocol suite, which is the basis for the Internet.

The four layers of the TCP/IP model, in order from top to bottom, are:
| Layer Name | Commonly used protocol  |
|---------|----------|
| Application Layer | HTTP, DNS, SMTP, SSH  |
| Transport Layer | TCP, UDP  |
| Network Layer | IP, ICMP  |
| Network Interface Layer | Ethernet  |

#### *Visiting google.com in the browser - it's really much more complicated*

What happens when you open your web browser and type http://www.google.com? We will try to examine it in terms of the OSI model.

**Application Layer**
The browser uses HTTP protocol to form an HTTP request to Google’s servers, to serve Google's home page. The HTTP request is merely a text in a well-defined form, it may look like:
```http
GET / HTTP/1.1
Host: google.com
User-Agent: Mozilla/5.0
```
Note that we literally want to transfer this text to Google’s servers, as is. On the server side, there is an application (called "webserver", obviously) that knows how to respond to this kind of text. Since web browsers and web servers are applications that use the network, it resides in the application-layer.

The application layer is where network applications and their application-layer protocols reside. Network applications may be Web browsers, web servers, mails, and every application that sends or receives data over the Internet, in any kind and form.

Do your Firefox or Chrome browsers know how exactly to transfer this kind of text over the Internet? Do Apache or Nginx servers know how to send responses over the Internet? Hell no! They both use the great service of the Transport layer.

**Transport Layer**
The HTTP text message is transferred, via a file of type socket (will be discussed soon), to another piece of "software" in the Linux kernel, this software is able to transport application-layer messages from one host to another using the TCP protocol. In simple words, TCP says: "no matter who you are, Outlook, WhatsApp, Firefox... give me a message to transfer, and a destination, and I'll be responsible to serve you and transfer this message for you. All you need is to talk with me according to my [strict rules protocol](https://www.ietf.org/rfc/rfc793.txt)".

TCP breaks long **messages** into shorter **segments**, it guarantees that the data was indeed delivered to the destination and controls the order in which segments are being sent. Note that TCP only controls **how** the data is being sent and received, but it is not responsible for the actual sending of the data. To send its segments, TCP uses the service of a very close friend - IP.

The transport layer controls the transportation of application-layer messages between application endpoints.

There are two major protocols in this layer:
- TCP (Transmission Control Protocol), which is a reliable, connection-oriented transport layer protocol that provides a guaranteed delivery of data and error detection mechanisms.
- UDP (User Datagram Protocol), which is a lightweight, connectionless transport layer protocol, used for fast, low-latency communication and is commonly used for video streaming, online gaming, and other real-time applications.

**Internet Layer**
We continue our journey to get Google.com's homepage. So we have TCP segments ready to be transferred to Google's servers.

The IP protocol is responsible for moving the TCP segments from one host to another. Just as you would give the postal service a letter with a destination address, IP protocol sends a piece of data (a.k.a packets) to an address (a.k.a IP addresses). Like TCP, IP is a piece of software that resides in the linux kernel (so close to TCP, that they are frequently called TCP/IP). In order to send **packets** over the Internet, IP communicates with a **network interface**, which is a software abstraction that represents a physical (or virtual) network device, such as an Ethernet card or a wireless adapter.

The network layer routes packets through a series of routers between the source and destination hosts.

**Network Interface Layer**
The network interface layer is the lower level component in our model. It provides an interface between the physical network and the higher-level networking protocols. It handles the transmission and reception of data **frames** over the network, and it is responsible for converting **digital signals** into **analog signals** for transmission over the physical network.

In this layer, every physical (or virtual) network device has a media access control (**MAC**) address. MAC address is the unique identifier assigned to a network interface. MAC addresses are assigned at the time that a network adapter is manufactured or, if it's virtualized, the time that it is created.