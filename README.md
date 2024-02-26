# Containerized image processing

A simple container providing a REST API for image -> image processing algorithms.

After building and tagging the image (e.g., as `imageprocessing`), run it and map your desired port to 8000:

Example:

```
docker run --rm -p 8000:8000 imageprocessing
```

Then issue a POST request to the `/dither/` endpoint containing an image, and you will receive a dithered image in .png format. Other algorithms are left as an exercise to the reader.

Note that the dithering algorithm is slow and is designed for small grayscale images.
