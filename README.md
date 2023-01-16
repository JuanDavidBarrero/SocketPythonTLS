# Importan 

```
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out certificate.crt
```
si se va a usar una ip para el certificado es necesari hacer los siguiente pasos
-   Crar un archivo de configuración **san.cnf**
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
-   Ejecutar el siguiente comando 
```
openssl req -x509 -nodes -days 730 -newkey rsa:2048 -keyout key.pem -out cert.pem -config san.cnf
```
-   Cambiar respectivamente los nombres en el códgio de servidor y cliente
