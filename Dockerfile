# Use the Node.js 20 Alpine version for smaller image size
FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Next.js app
RUN npm run build

# Expose the port and start the app
EXPOSE 3000
CMD ["npm", "run", "start"]
