FROM julia:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Julia script into the container
COPY app.jl .

# Install Julia packages
RUN julia -e 'using Pkg; Pkg.add(["HTTP", "Images", "FileIO", "ImageIO"])'

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Julia script when the container launches
CMD ["julia", "app.jl"]