Chuyên đề 1
======

nhóm 6
-----

+ cài đặt cho Linux (Ubuntu 18.04): 
    1. di chuyển vào thư mục này "ImageAI" tạo môi trường ảo Python3
    ```bash
    python3 -m venv env && source env/bin/activate
    ```
    2. cài đặt các gói:
    ```bash
    pip install --upgrade tensorflow numpy scipy opencv-python pillow matplotlib h5py keras https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl
    ```
    3. chạy các câu lệnh cho các bộ đếm khác nhau:
    - Bộ đếm xe máy: 
    ```bash
    python image_custom_object_detection.py
    ```
    
    > kết quả: <br> ![](https://we25.vn/media/files/co-gai-xinh-dep-2.jpg "An optional title")

    > code: <br> ![](https://we25.vn/media/files/co-gai-xinh-dep-2.jpg "An optional title")

    - Bộ đếm xe máy, xe bus, xe tải, oto:
    ```bash
    python auto_dir.py
    ```

    > kết quả: <br> ![](https://we25.vn/media/files/co-gai-xinh-dep-2.jpg "An optional title")

    > code: <br> ![](https://we25.vn/media/files/co-gai-xinh-dep-2.jpg "An optional title")


## Many thanks to [ImageAI]( https://github.com/OlafenwaMoses/ImageAI )