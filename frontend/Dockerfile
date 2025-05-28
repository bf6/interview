FROM node:24-bullseye

# Install pnpm
RUN npm install -g pnpm

# Set work directory
WORKDIR /app

# Copy dependency files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy project
COPY . .

# Expose port
EXPOSE 5173

# Start the app in development mode
CMD ["pnpm", "dev", "--host"]