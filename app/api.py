import asyncio
from concurrent.futures import ProcessPoolExecutor
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse
from io import BytesIO

from PIL import Image

from floyd_steinberg import floyd_steinberg_dithering

app = FastAPI()

executor = ProcessPoolExecutor(max_workers=5)

@app.post("/dither/")
async def dither_image(file: UploadFile = File(...)):
    image_bytes = await file.read()  # Read the image file as bytes
    input_image = Image.open(BytesIO(image_bytes))  # Open the image using PIL

    # Process the image w/o blocking the event loop
    loop = asyncio.get_event_loop()
    future = executor.submit(floyd_steinberg_dithering, input_image)
    processed_image = await loop.run_in_executor(None, future.result)
    
    output = BytesIO()
    processed_image.save(output, format="PNG")
    output.seek(0)

    return StreamingResponse(output, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)