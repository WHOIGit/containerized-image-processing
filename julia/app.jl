using HTTP
using Images
using FileIO
using ImageIO

function floyd_steinberg_dithering(img::AbstractArray)
    # Convert image to grayscale
    gray_img = Float64.(Gray.(img))

    # Get image dimensions
    rows, cols = size(gray_img)

    # Floyd-Steinberg Dithering
    for row in 1:rows
        for col in 1:cols
            old_pixel = gray_img[row, col]
            new_pixel = old_pixel > 0.5 ? 1.0 : 0.0
            gray_img[row, col] = new_pixel
            error = old_pixel - new_pixel
            if col + 1 <= cols
                gray_img[row, col + 1] += error * 7 / 16
            end
            if row + 1 <= rows && col - 1 >= 1
                gray_img[row + 1, col - 1] += error * 3 / 16
            end
            if row + 1 <= rows
                gray_img[row + 1, col] += error * 5 / 16
            end
            if row + 1 <= rows && col + 1 <= cols
                gray_img[row + 1, col + 1] += error * 1 / 16
            end
        end
    end

    return gray_img
end

function handle_request(request::HTTP.Request)
    # Parse multipart/form-data
    data = HTTP.parse_multipart_form(request)

    # if data is ::Nothing, then return 400
    if data == nothing
        return HTTP.Response(400, "No file found in the request. Please provide an image file.")
    end

    mktempdir() do temp_dir
        temp_file = joinpath(temp_dir, "temp_image.png")

        open(temp_file, "w") do file
            write(file, take!(data[1].data))
        end

        # Load the image from the temporary file

        img = FileIO.load(temp_file)

        dithered_img = floyd_steinberg_dithering(img)

        # Save the dithered image to a file

        FileIO.save(temp_file, dithered_img)

        img_bytes = read(temp_file)

        return HTTP.Response(200, HTTP.Headers(["Content-Type" => "image/png"]), img_bytes)
    end
end

const MY_ROUTER = HTTP.Router()
HTTP.register!(MY_ROUTER, "POST", "/dither", handle_request)

HTTP.serve(MY_ROUTER, "0.0.0.0", 8000)
