# Differences Between ALB, NLB, and Gateway Load Balancer

## Overview
Amazon Web Services (AWS) provides different types of load balancers to handle various use cases and application requirements. This document compares Application Load Balancer (ALB), Network Load Balancer (NLB), and Gateway Load Balancer (GWLB) in terms of their features, use cases, and functionalities.

## 1. Application Load Balancer (ALB)

- **Layer**: Operates at Layer 7 (Application Layer) of the OSI model.
- **Functionality**:
  - Distributes HTTP/HTTPS traffic based on content (URL paths, hostnames, HTTP headers).
  - Supports advanced routing features such as host-based routing and path-based routing.
  - Can handle WebSocket and HTTP/2 connections.
- **Use Cases**:
  - Ideal for microservices architectures and containerized applications.
  - Best suited for applications requiring complex routing and request transformations.
- **Health Checks**: Performs health checks at the application level to ensure only healthy targets receive traffic.
- **Integration**: Integrates with AWS services like AWS Certificate Manager (ACM) for SSL termination, AWS WAF for web application firewall capabilities, and Amazon ECS for container management.

## 2. Network Load Balancer (NLB)

- **Layer**: Operates at Layer 4 (Transport Layer) of the OSI model.
- **Functionality**:
  - Distributes TCP/UDP traffic based on IP protocol data.
  - Capable of handling millions of requests per second with ultra-low latency.
  - Provides static IP addresses for the load balancer.
- **Use Cases**:
  - Ideal for applications that require extreme performance and need to handle TCP/UDP traffic (e.g., gaming, IoT, VoIP).
  - Best suited for load balancing traffic for non-HTTP protocols.
- **Health Checks**: Performs health checks at the connection level to ensure the availability of backend targets.
- **Integration**: Can be integrated with AWS Global Accelerator for improved availability and performance.

## 3. Gateway Load Balancer (GWLB)

- **Layer**: Operates at Layer 3 (Network Layer) of the OSI model.
- **Functionality**:
  - Combines the features of a transparent network gateway with load balancing capabilities.
  - Allows users to deploy, scale, and manage third-party virtual appliances (e.g., firewalls, intrusion detection systems).
  - Transparent to the traffic it processes, making it easy to insert into existing architectures.
- **Use Cases**:
  - Ideal for integrating third-party network appliances for security and monitoring.
  - Best suited for hybrid environments where network traffic needs to be inspected or processed.
- **Health Checks**: Performs health checks at the endpoint level to ensure availability of the appliance.
- **Integration**: Integrates seamlessly with virtual appliances and can be used in conjunction with VPC and VPN architectures.

## Summary of Differences

| Feature                   | Application Load Balancer (ALB) | Network Load Balancer (NLB) | Gateway Load Balancer (GWLB) |
|---------------------------|----------------------------------|------------------------------|-------------------------------|
| **Layer**                 | Layer 7 (Application Layer)      | Layer 4 (Transport Layer)    | Layer 3 (Network Layer)       |
| **Traffic Type**          | HTTP/HTTPS                        | TCP/UDP                      | TCP/UDP                       |
| **Routing**               | Content-based routing             | Connection-based routing      | Transparent gateway            |
| **Use Case**              | Microservices, web applications   | High-performance applications | Network appliance integration   |
| **Health Checks**         | Application-level                 | Connection-level              | Endpoint-level                 |
| **Integration**           | AWS services, WAF                | AWS Global Accelerator        | Third-party virtual appliances  |

## Conclusion

Choosing the right load balancer depends on the specific requirements of your application. ALB is best for HTTP/HTTPS applications with advanced routing needs, NLB is suitable for high-performance TCP/UDP applications, and GWLB is ideal for integrating network appliances into your architecture.
