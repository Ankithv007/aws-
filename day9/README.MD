# S3 Bucket Static Website Hosting

## Overview

This repository provides the setup and configuration for hosting a static website using Amazon S3.
The S3 bucket named `staticwebakith` is configured to serve static content such as HTML, CSS, and JavaScript files.

## Bucket Name

- **Bucket Name**: `staticwebakith`  /// change if you want but name should be uniquw because its create separate url its may goes to dns service

## Configuration

### Static Website Hosting

1. **Configuration Steps:**

   - Select the bucket `staticwebakith`.  /// as ypur wish i choose the staticwebakith the name should be unique
   - Navigate to the **Properties** tab.
   - Under **Static website hosting**, configure the bucket as follows:
     - **Index document**: `index.html`
     - (Optional) **Error document**: `error.html` (if you have a custom error page)

2. **Bucket Policy:**
   To allow public access to the files in the bucket, add the following bucket policy:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::staticwebakith/*"    ///change the name as per the bucket name as you created before
       }
     ]
   }

