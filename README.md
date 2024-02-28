# Containerized image processing

A simple container providing a REST API for image -> image processing algorithms.

After building and tagging the image (e.g., as `imageprocessing`), run it and map your desired port to 8000:

Example:

```
docker run --rm -p 8000:8000 imageprocessing
```

Then issue a POST request to the `/dither/` endpoint containing an image, and you will receive a dithered image in .png format. Other algorithms are left as an exercise to the reader. For example:

```
curl -X POST -F "file=@some_image_file.jpg" http://localhost:8000/dither/ > output.png
```

Note that the dithering algorithm is slow and is designed for small grayscale images.

## Kubernetes

To deploy in Kubernetes, first build the image and tag it as `imageprocessing`:

```
docker build -t imageprocessing:latest .
```

Next, bring the deployment and service up:

```
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```

Now forward port 8000 to the service:

```
kubectl port-forward service/imageproc-service 8000:8000
```

To test, make a POST request as described above.

To bring the deployment down:

```
kubectl delete deployment imageproc-deployment
kubectl delete service imageproc-service
```