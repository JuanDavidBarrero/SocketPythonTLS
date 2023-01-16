# Importan !


## Local Test
If you are going to do local testing to generate the private key and certificates you can use the following command

```
    openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out certificate.crt
```
## External server

if you are going to use an ip for the certificate you need to do the following steps
- Create a configuration file **san.cnf**

```
    [req]
    default_bits  = 2048
    distinguished_name = req_distinguished_name
    req_extensions = req_ext
    x509_extensions = v3_req
    prompt = no
    [req_distinguished_name]
    countryName = XX
    stateOrProvinceName = N/A
    localityName = N/A
    organizationName = Self-signed certificate
    commonName = 120.0.0.1: Self-signed certificate
    [req_ext]
    subjectAltName = @alt_names
    [v3_req]
    subjectAltName = @alt_names
    [alt_names]
    IP.1 = ** HERE THE IP **
```
-    Execute the following command 

```
    openssl req -x509 -nodes -days 730 -newkey rsa:2048 -keyout key.pem -out cert.pem -config san.cnf
```
-   Change respectively the names in the **serverTLS.py** and **clientTLS.py** codes
