# Containerized image processing

A simple container for performing an image processing operation on a set of input files and depositing them in an output directory.

To use, map your input and output directories to `/input` and `/output` container paths.

Example:

```
docker build -t image-processing .
docker run --rm -v ./input:/input -v ./output:/output image-processing
```

Operations and errors are logged to to `/logs` in the container, so can be exposed by adding `-v /my/log/dir:/logs` to the `docker run` command.
