# Use the official Nginx image as the base image
FROM nginx:alpine

# Copy the index.html to the Nginx HTML directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
