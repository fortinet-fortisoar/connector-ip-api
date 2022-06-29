## About the connector
IP-API helps to get the following information for any IP address: city, region (name & code), country (name & code), continent, postal code / zip code, latitude, longitude, time zone,  utc offset, european union (EU) membership, country calling code, country capital, country tld (top-level domain), currency (name & code), area & population of the country, languages spoken, asn, organization and hostname. This connector facilitates automated operation related to ip-api.
<p>This document provides information about the IP-API Connector, which facilitates automated interactions, with a IP-API server using FortiSOAR&trade; playbooks. Add the IP-API Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with IP-API.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-ip-api`

## Prerequisites to configuring the connector
- You must have the URL of IP-API server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the IP-API server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>IP-API</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>URL of the IP-API connector to access the connector website.<br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Execute Batch API<br></td><td>Execute batch API to query multiple IP addresses in one HTTP request. This is significantly faster than submitting individual queries.<br></td><td>execute_batch_api <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Execute Batch API
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>List of Ip Addresses<br></td><td>Required list of ip addresses eg: ['8.8.8.8', '24.48.0.1'].<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "country": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "countryCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "region": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "regionName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "city": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "zip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "lat": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "lon": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timezone": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "isp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "org": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "as": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - ip-api - 1.0.0` playbook collection comes bundled with the IP-API connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the IP-API connector.

- Batch:

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
