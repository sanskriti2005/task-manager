# Use official Node image
FROM node:20

# Set working directory inside container
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of your frontend code
COPY . .

# Expose the port your frontend uses
EXPOSE 5173

# Start the development server
CMD ["npm", "run", "dev"]
